# ComfyUI AI Assistants – Knowledge Base (v1)
_Last updated: 2025-08-12_

> **Scope:** Жива база знания за AI асистенти и интеграции около ComfyUI (генериране на изображения, автоматизация и създаване на workflows). Този файл е структуриран за лесно ползване от GPT/Claude/Gemini и за автоматично **добавяне на ъпдейти в края** (виж секция “Updates”).

## Quick picks (TL;DR)
- **Най-универсален за дебъг/код:** GPT-5 / GPT-4o (ChatGPT).
- **Дълги контексти и аналитика на големи workflow-и:** Claude 3.5 Sonnet.
- **Мултимодалност и бързо image editing вътре в ComfyUI:** Gemini 2.x + Gemini нод.
- **Локално и без облак:** Mistral / Magistral (през LLM Loader / LLM Party).
- **Вграден UI асистент:** ComfyUI Copilot (Alibaba).

## Decision matrix (кратка)
| Задача | Най-подходящ | Алтернативи |
|---|---|---|
| Генериране на подробни prompt-ове | GPT-5/4o | Claude |
| Обяснение/дебъг на сложен workflow | Claude 3.5 | GPT-5 |
| „Едно-изречение → редакция на изображение“ | Gemini | GPT-4o |
| Локален офлайн помощник | Mistral/Magistral | Qwen, Llama |
| Генериране на ComfyUI workflow от текст | ComfyUI Copilot | ComfyCopilot (външен) |
| Текстов нод в самия workflow | ChatGPT Helper node | LLM Party + локален LLM |

---

## LLM асистенти (overview)
### ChatGPT (GPT-5 / 4o)
- **Use-cases:** дебъг на грешки (Python/CUDA), писане/рефактор на custom nodes, разбиране на скрийншоти от графи, добър prompt engineering.
- **Кога да го викаш:** когато workflow-ът „гърми“, когато искаш да генерираш clean JSON за ComfyUI или да оптимизираш VRAM/скорост.

### Claude 3.5 Sonnet
- **Use-cases:** огромни контексти (цели workflow-и, логове), структурирани обяснения, документация.
- **Кога:** анализ на дълги проекти; хладнокръвни, безопасни обяснения.

### Gemini 2.x
- **Use-cases:** мултимодални задачи (текст+изображения), директни редакции през Gemini нода; бърз визуален feedback.
- **Кога:** когато искаш „вътре в ComfyUI“ да редактираш/генерираш изображения с кратки инструкции.

### Mistral / Magistral (отворени)
- **Use-cases:** локален офлайн асистент, chain-of-thought reasoning, добър баланс качество/ресурс.
- **Кога:** когато искаш поверителност и без API разходи.

### LLaVA / VLM (визуален LLM)
- **Use-cases:** авто-анализ на изображенията от ComfyUI („критик“), OCR, превръщане на картинка в текст за следваща стъпка.

---

## Специализирани решения и нодове
### ComfyUI Copilot (Alibaba)
- **Какво прави:** интерактивен UI помощник; генерира workflows от текст; дава оптимизации и шаблони.
- **Кога:** бърз старт, обучение, стандартни pipeline-и.

### ChatGPT Helper (custom node)
- **Какво:** подава кратък текст → връща богат prompt; преводи/стилизации/вариации в самия workflow.
- **Кога:** когато искаш динамични prompt-ове или текстова логика без да напускаш ComfyUI.

### ComfyCopilot (външен „text→workflow“)
- **Какво:** генерира .json граф от текстово описание (за бърз прототип).
- **Кога:** за стартова основа, после ръчна донастройка.

### ComfyUI Agent (общностен)
- **Какво:** наблюдава графа, дава обяснения/съвети/предупреждения в реално време.
- **Кога:** за debug и обучение в движение.

### LLM Party / LLM Loader (интеграция на LLM в ComfyUI)
- **Какво:** възли за работа с локални и cloud LLM, вкл. VLM.
- **Кога:** когато строиш „вътрешен“ чат-агент в самия workflow.

> **Бележка:** Добавяй линкове към конкретни репота тук, когато ги използваш:
- ComfyUI Copilot – [ADD_URL]
- ChatGPT Helper node – [ADD_URL]
- LLM Party – [ADD_URL]
- Gemini API node – [ADD_URL]
- ComfyCopilot – [ADD_URL]
- ComfyUI Agent – [ADD_URL]

---

## Prompt Kit (копирай и ползвай)
### 1) Knowledge-only отговор
**System/User:** „Използвай само прикачената/посочената база знания (knowledge.md). Ако инфото липсва, кажи точно какво да се добави. Не импровизирай.“

### 2) Избор на инструмент
„На база на моята база знания, предложи най-подходящия асистент за: _[задача]_. Дай 3 опции с плюсове/минуси, нужни нодове и очаквано качество/ресурс.“

### 3) Генериране на ComfyUI workflow JSON (v1)
„Създай валиден ComfyUI workflow JSON v1 за _[цел]_. Използвай налични нодове. Върни **само JSON**. Обясненията – отделно, след JSON.“

### 4) Debug на грешка
„Анализирай този лог / описание на проблем. Дай хипотеза → проверка → fix. Ако липсват данни, кажи точно какво да логна/покажа.“

### 5) Image critique → prompt
„Оцени това изображение (качвам го): как да подобря реализъм/анатомия/шум? Дай конкретни промени в prompt/параметри/нодове.“

---

## Мини „рецепти“ (short workflows)
- **Лицева консистентност (множество изображения):** face embed/ID + consistent seed + refiner накрая; опция: IP-Adapter/FaceID.
- **Интеграция на реален продукт:** segment+inpaint; изчистен маск; светлинно съвпадение; финал – high-res fix/upscale.
- **Пълна автоматизация:** scheduler → промпт генератор (LLM нод) → SD pipeline → критик (VLM) → авто-корекция на prompt/параметри → export.

---

## Как да използва GPT/Claude/Gemini с този файл
1) Дай линк към RAW на `knowledge.md` **или** го прикачи.
2) В инструкциите/първо съобщение добави „Knowledge-only“ отгоре.
3) Ако е възможно – включи web browsing и кажи „винаги първо отвори RAW URL и използвай това като първичен източник“.

---

## Updates (auto-append below)
> **Автоматизации (Zapier/Make):** настрой да **добавяш нов ред в края на файла** при новина/релийз. Не променяй секциите над това място.

- 2025-08-12: Initialized knowledge base. _auto-added_
- 2025-08-16T06:07:12+00:00: record audio node (#8716) - https://github.com/comfyanonymous/ComfyUI/commit/20a84166d0d37dd6833caa6cadf3bfac8c241b48 __auto-added__
- 2025-08-13T15:45:51+00:00: v0.3.50 - https://github.com/comfyanonymous/ComfyUI/releases/tag/v0.3.50 __auto-added__
- 2025-08-16T03:23:15+00:00: v1.26.4 - https://github.com/Comfy-Org/ComfyUI_frontend/releases/tag/v1.26.4 __auto-added__
- 2025-08-16: Добави ръководство за RunPod (GPU Pod, persistent volume, порт 8188, стартов скрипт, ComfyUI-Manager, пътища за модели).

- 2025-08-13T18:50:55+00:00: v0.4.62 - https://github.com/Comfy-Org/desktop/releases/tag/v0.4.62 __auto-added__
- 2025-08-13T14:34:09+00:00: ComfyUI Wan2.2 Fun Native Support and LightX2V 4-Step LoRA Integration - https://blog.comfy.org/p/comfyui-wan22-fun-inp-support __auto-added__
- 2025-08-16T21:51:28+00:00: Qwen image model refactor. (#9375) - https://github.com/comfyanonymous/ComfyUI/commit/0f2b8525bcafe213e8421a49564a90f926e81f2e __auto-added__