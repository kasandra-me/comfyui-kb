import os, sys, time, datetime
import feedparser

KNOWLEDGE_FILE = os.environ.get("KNOWLEDGE_FILE", "knowledge.md")
MAX_ITEMS_PER_FEED = int(os.environ.get("MAX_ITEMS_PER_FEED", "1"))

def iso_from_entry(e):
    for k in ("updated_parsed", "published_parsed"):
        t = getattr(e, k, None)
        if t:
            dt = datetime.datetime.fromtimestamp(time.mktime(t), datetime.timezone.utc)
            return dt.isoformat()
    return datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc).isoformat()

def load_text(path):
    if not os.path.exists(path):
        return ""
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def save_text(path, text):
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)

def main():
    feeds_raw = os.environ.get("FEEDS", "").strip()
    if not feeds_raw:
        print("No FEEDS provided.", file=sys.stderr)
        sys.exit(1)

    feeds = [u.strip() for u in feeds_raw.splitlines() if u.strip()]
    content = load_text(KNOWLEDGE_FILE)
    original_content = content
    added = 0

    # Дефинираме приоритетни keywords извън loop-а
    PRIORITY_KEYWORDS = ["runpod", "torch", "cuda", "performance", "breaking", "security"]

    for url in feeds:
        d = feedparser.parse(url)
        if d.bozo:
            print(f"[warn] Problem parsing feed: {url}")
            continue
        entries = d.entries[:MAX_ITEMS_PER_FEED] if d.entries else []
        for e in entries:
            link = getattr(e, "link", "").strip()
            title = getattr(e, "title", "").strip() or "(no title)"
            published = iso_from_entry(e)

            # ако линкът вече съществува в файла — пропускаме (без дублиране)
            if link and link in content:
                continue

            # Проверка за приоритетни keywords
            if any(kw.lower() in title.lower() for kw in PRIORITY_KEYWORDS):
                line = f"- 🔥 {published}: {title} - {link} __priority-auto-added__"
            else:
                line = f"- {published}: {title} - {link} __auto-added__"
            
            content += ("\n" if content and not content.endswith("\n") else "") + line
            added += 1

    if content != original_content:
        save_text(KNOWLEDGE_FILE, content)
        print(f"Added {added} new line(s).")
    else:
        print("No new items to add.")

if __name__ == "__main__":
    main()
