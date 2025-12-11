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
- 2025-08-17T20:45:39+00:00: WIP Qwen edit model: The diffusion model part. (#9383) - https://github.com/comfyanonymous/ComfyUI/commit/ed43784b0d04e5b8e8ff2c057fa84b9c5132aaf2 __auto-added__
- 2025-08-17T21:38:40+00:00: Update template to 0.1.60 (#9377) - https://github.com/comfyanonymous/ComfyUI/commit/d4e353a94ec5a8cb15ed151990a9518b890e5d4f __auto-added__
- 2025-08-17T22:54:07+00:00: Make step index detection much more robust (#9392) - https://github.com/comfyanonymous/ComfyUI/commit/7f3b9b16c6636cb1201213574892d33c2a35e4ba __auto-added__
- 2025-08-18T03:21:02+00:00: Bump frontend to 1.25.9 (#9394) - https://github.com/comfyanonymous/ComfyUI/commit/da2efeaec6609265051165bfb413a2a4c84cf4bb __auto-added__
- 2025-08-18T02:57:44+00:00: v1.25.9 - https://github.com/Comfy-Org/ComfyUI_frontend/releases/tag/v1.25.9 __auto-added__
- 2025-08-18T07:26:55+00:00: fix(WAN-nodes): invalid nodeid for WanTrackToVideo (#9396) - https://github.com/comfyanonymous/ComfyUI/commit/bd2ab73976a4e245db3e057795328c89bfd98a88 __auto-added__
- 2025-08-19T02:38:34+00:00: P2 of qwen edit model. (#9412) - https://github.com/comfyanonymous/ComfyUI/commit/4977f203fa8e9e3ab22884c8ace8f9b540d48952 __auto-added__
- 2025-08-19T06:54:08+00:00: v1.26.5 - https://github.com/Comfy-Org/ComfyUI_frontend/releases/tag/v1.26.5 __auto-added__
- 2025-08-14T21:06:55+00:00: 5.4.0 - https://github.com/runpod-workers/worker-comfyui/releases/tag/5.4.0 __auto-added__
- 2025-08-19T20:30:06+00:00: feat(api-nodes): add Vidu Video nodes (#9368) - https://github.com/comfyanonymous/ComfyUI/commit/54d8fdbed0a7b171ab8cfb02e29a7e0dc5fe78fd __auto-added__
- 2025-08-19T20:49:01+00:00: Change the TextEncodeQwenImageEdit node to use logic closer to refere… - https://github.com/comfyanonymous/ComfyUI/commit/bddd69618bf4463209c3681babfcbebd9b9aed85 __auto-added__
- 2025-08-20T00:47:42+00:00: Rope fix for qwen vl. (#9435) - https://github.com/comfyanonymous/ComfyUI/commit/dfa791eb4bfcaac3eb9b2b33fa15ae5a25589bb8 __auto-added__
- 2025-08-20T01:59:23+00:00: The Comfy Challenge Week #1 - https://blog.comfy.org/p/the-comfy-challenge-week-1 __auto-added__
- 2025-08-20T04:45:27+00:00: Qwen rotary embeddings should now match reference code. (#9437) - https://github.com/comfyanonymous/ComfyUI/commit/7cd2c4bd6ab20f35a6bb1b1f2252c3ea16da4777 __auto-added__
- 2025-08-20T05:08:11+00:00: Disable prompt weights for qwen. (#9438) - https://github.com/comfyanonymous/ComfyUI/commit/5a8f502db5889873ffa13132b603b7b6daac605a __auto-added__
- 2025-08-20T07:15:30+00:00: ComfyUI version 0.3.51 - https://github.com/comfyanonymous/ComfyUI/commit/7139d6d93fc7b5481a69b687080bd36f7b531c46 __auto-added__
- 2025-08-20T07:15:30+00:00: v0.3.51 - https://github.com/comfyanonymous/ComfyUI/releases/tag/v0.3.51 __auto-added__
- 2025-08-20T07:33:10+00:00: LTXV: fix key frame noise mask dimensions for when real noise mask ex… - https://github.com/comfyanonymous/ComfyUI/commit/fe01885acf892de636b1b2743903812099bd42e3 __auto-added__
- 2025-08-20T09:32:30+00:00: v0.4.63 - https://github.com/Comfy-Org/desktop/releases/tag/v0.4.63 __auto-added__
- 2025-08-20T14:10:13+00:00: Qwen-Image-Edit ComfyUI Native Support - https://blog.comfy.org/p/qwen-image-edit-comfyui-support __auto-added__
- 2025-08-20T21:34:13+00:00: Add that qwen edit model is supported to readme. (#9463) - https://github.com/comfyanonymous/ComfyUI/commit/e73a9dbe30434280c69d852ea78cc4bf88bfd501 __auto-added__
- 2025-08-21T03:09:35+00:00: Forgot this. (#9470) - https://github.com/comfyanonymous/ComfyUI/commit/9fa1036f60b5264302072453be524aa55928bbaf __auto-added__
- 2025-08-21T04:33:49+00:00: Support diffsynth inpaint controlnet (model patch). (#9471) - https://github.com/comfyanonymous/ComfyUI/commit/1b2de2642d38099acdde7c460d133d93e91074f0 __auto-added__
- 2025-08-21T06:22:53+00:00: v1.26.6 - https://github.com/Comfy-Org/ComfyUI_frontend/releases/tag/v1.26.6 __auto-added__
- 2025-08-21T23:00:07+00:00: ComfyUI 0.3.51: Subgraph, New Manager UI, Mini Map and More - https://blog.comfy.org/p/comfyui-035-frontend-updates __auto-added__
- 2025-08-22T03:18:04+00:00: Make it easier to implement future qwen controlnets. (#9485) - https://github.com/comfyanonymous/ComfyUI/commit/f7bd5e58dd03e799e02f6851b84b51e14ad0da7b __auto-added__
- 2025-08-22T04:53:11+00:00: Support InstantX Qwen controlnet. (#9488) - https://github.com/comfyanonymous/ComfyUI/commit/ff57793659702d502506047445f0972b10b6b9fe __auto-added__
- 2025-08-22T18:08:21+00:00: Unlimited Parallel API Nodes & New Model Options - https://blog.comfy.org/p/unlimited-parallel-api-nodes-and __auto-added__
- 2025-08-22T17:51:14+00:00: feat(api-nodes): add copy button to Gemini Chat node (#9440) - https://github.com/comfyanonymous/ComfyUI/commit/050c67323c33f6543309d4f09df706ec8c9a1389 __auto-added__
- 2025-08-22T21:40:18+00:00: Update template to 0.1.65 (#9501) - https://github.com/comfyanonymous/ComfyUI/commit/ca4e96a8ae6c9ee8d40fe35100ed9b2247e71e40 __auto-added__
- 2025-08-22T23:39:15+00:00: Add elementwise fusions (#9495) - https://github.com/comfyanonymous/ComfyUI/commit/fe31ad02768c66c61b3dc12f5d4bdfe8990ce25c __auto-added__
- 2025-08-23T02:41:08+00:00: Implement EasyCache and Invent LazyCache (#9496) - https://github.com/comfyanonymous/ComfyUI/commit/fc247150fec502b1834390516b556a87003f1d79 __auto-added__
- 2025-08-23T03:15:44+00:00: Fix Conditioning masks on 3d latents. (#9506) - https://github.com/comfyanonymous/ComfyUI/commit/41048c69b4ccf63f876213a95a51cdde1cb0ab84 __auto-added__
- 2025-08-23T05:36:44+00:00: Python 3.13 is well supported. (#9511) - https://github.com/comfyanonymous/ComfyUI/commit/59eddda90030b61f172e155bc1e2526a51a27dff __auto-added__
- 2025-08-23T17:56:17+00:00: Don't use the annoying new navigation mode by default. (#9518) - https://github.com/comfyanonymous/ComfyUI/commit/8be0d22ab76a3d548c9c376fd816b39d4c028c12 __auto-added__
- 2025-08-23T21:03:22+00:00: v1.25.10 - https://github.com/Comfy-Org/ComfyUI_frontend/releases/tag/v1.25.10 __auto-added__
- 2025-08-23T21:54:01+00:00: Update frontend to v1.25.10 and revert navigation mode override (#9522) - https://github.com/comfyanonymous/ComfyUI/commit/3e316c6338503a535801db3ddac9572a38a607ef __auto-added__
- 2025-08-23T22:57:09+00:00: ComfyUI version 0.3.52 - https://github.com/comfyanonymous/ComfyUI/commit/71ed4a399ec76a75aa2870b772d2022e4b9a69a3 __auto-added__
- 2025-08-23T22:57:09+00:00: v0.3.52 - https://github.com/comfyanonymous/ComfyUI/releases/tag/v0.3.52 __auto-added__
- 2025-08-24T00:30:37+00:00: v0.4.64 - https://github.com/Comfy-Org/desktop/releases/tag/v0.4.64 __auto-added__
- 2025-08-24T19:29:49+00:00: Fix EasyCache/LazyCache crash when tensor shape/dtype/device changes … - https://github.com/comfyanonymous/ComfyUI/commit/95ac7794b7c735de8e5426442507d08edd29bec5 __auto-added__
- 2025-08-24T19:40:32+00:00: Remove models from readme that are not fully implemented. (#9535) - https://github.com/comfyanonymous/ComfyUI/commit/f6b93d41a03081fad3c1a01221eac9c42d6790df __auto-added__
- 2025-08-25T20:50:48+00:00: Qwen Image ControlNet & LoRA, EasyCache and Context Window in ComfyUI - https://blog.comfy.org/p/comfyui-now-supports-qwen-image-controlnet __auto-added__
- 2025-08-26T03:26:47+00:00: Implement wav2vec2 as an audio encoder model. (#9549) - https://github.com/comfyanonymous/ComfyUI/commit/914c2a29731be9c082f773c4b95892f553ac5ae8 __auto-added__
- 2025-08-26T16:50:46+00:00: Make AudioEncoderOutput usable in v3 node schema. (#9554) - https://github.com/comfyanonymous/ComfyUI/commit/39aa06bd5d630e50c88d3be1586d21737c4387c1 __auto-added__
- 2025-08-26T17:33:54+00:00: Update template to 0.1.66 (#9557) - https://github.com/comfyanonymous/ComfyUI/commit/5352abc6d389570455776c457738db54367cd6cb __auto-added__
- 2025-08-26T17:56:39+00:00: Day-1 Support of Qwen-Image InstantX ControlNet - https://blog.comfy.org/p/day-1-support-of-qwen-image-instantx __auto-added__
- 2025-08-27T02:20:44+00:00: Adding Google Gemini Image API node (#9566) - https://github.com/comfyanonymous/ComfyUI/commit/47f4db3e84874ca6076e5cdbb345444faec83028 __auto-added__
- 2025-08-27T01:51:08+00:00: v1.25.11 - https://github.com/Comfy-Org/ComfyUI_frontend/releases/tag/v1.25.11 __auto-added__
- 2025-08-27T02:36:09+00:00: Nano-banana via ComfyUI API Nodes! - https://blog.comfy.org/p/nano-banana-via-comfyui-api-nodes __auto-added__
- 2025-08-27T04:10:20+00:00: Update template to 0.1.68 (#9569) - https://github.com/comfyanonymous/ComfyUI/commit/6a193ac557b2b35a6d2ea1916b0b8d5d9ee9b1ba __auto-added__
- 2025-08-27T05:10:34+00:00: WIP Wan 2.2 S2V model. (#9568) - https://github.com/comfyanonymous/ComfyUI/commit/88aee596a30e9b80ca831c42a0ae70e0d22b61ae __auto-added__
- 2025-08-27T07:41:37+00:00: v0.4.65 - https://github.com/Comfy-Org/desktop/releases/tag/v0.4.65 __auto-added__
- 2025-08-27T15:06:36+00:00: v1.26.7 - https://github.com/Comfy-Org/ComfyUI_frontend/releases/tag/v1.26.7 __auto-added__
- 2025-08-27T16:45:02+00:00: Fix #9537 (#9576) - https://github.com/comfyanonymous/ComfyUI/commit/b20ba1f27cbd4e1c84cf8ec72b345723de9e7c80 __auto-added__
- 2025-08-27T19:26:28+00:00: Fixes to make controlnet type models work on qwen edit and kontext. (… - https://github.com/comfyanonymous/ComfyUI/commit/b5ac6ed7ce73294e0025ffe3b16452d8434b83c7 __auto-added__
- 🔥 2025-08-27T20:06:40+00:00: Improve s2v performance when generating videos longer than 120 frames… - https://github.com/comfyanonymous/ComfyUI/commit/496888fd68813033c260195bf70e4d11181e5454 __priority-auto-added__
- 2025-08-27T23:07:31+00:00: Add DPM++ 2M SDE Heun (RES) sampler (#9542) - https://github.com/comfyanonymous/ComfyUI/commit/3aad339b63f03e17dc6ebae035b90afc2fefb627 __auto-added__
- 2025-08-28T03:09:06+00:00: ComfyUI 0.3.53 - https://github.com/comfyanonymous/ComfyUI/commit/0eb821a7b6612af0fa3aaa8302739788a4bd629e __auto-added__
- 2025-08-28T03:09:06+00:00: v0.3.53 - https://github.com/comfyanonymous/ComfyUI/releases/tag/v0.3.53 __auto-added__
- 2025-08-28T03:50:48+00:00: v0.4.66 - https://github.com/Comfy-Org/desktop/releases/tag/v0.4.66 __auto-added__
- 2025-08-28T04:39:12+00:00: "Turn It Around": The Comfy Challenge #1 Montage - https://blog.comfy.org/p/the-comfy-challenge-2-falling __auto-added__
- 2025-08-28T14:37:42+00:00: Fix diffsynth controlnet regression. (#9597) - https://github.com/comfyanonymous/ComfyUI/commit/ce0052c087cb1e81ba01e8afbe362bec54eeb665 __auto-added__
- 2025-08-28T14:44:57+00:00: ComfyUI version 0.3.54 - https://github.com/comfyanonymous/ComfyUI/commit/00636101771cb373354d6294cc6567deda2635f6 __auto-added__
- 2025-08-28T14:44:57+00:00: v0.3.54 - https://github.com/comfyanonymous/ComfyUI/releases/tag/v0.3.54 __auto-added__
- 2025-08-28T17:28:28+00:00: v0.4.67 - https://github.com/Comfy-Org/desktop/releases/tag/v0.4.67 __auto-added__
- 2025-08-28T21:59:48+00:00: WanSoundImageToVideoExtend node to manually extend s2v video. (#9606) - https://github.com/comfyanonymous/ComfyUI/commit/edde0b50431e296f61f79205e25cb01f653013a2 __auto-added__
- 2025-08-28T22:34:01+00:00: Fix issue with s2v node when extending past audio length. (#9608) - https://github.com/comfyanonymous/ComfyUI/commit/1c184c29eb2a8f6fdd4e49f27347809090038e3f __auto-added__
- 2025-08-28T23:38:28+00:00: Add a LatentCut node to cut latents. (#9609) - https://github.com/comfyanonymous/ComfyUI/commit/d28b39d93dc498110e28ca32c8f39e6de631aa42 __auto-added__
- 2025-08-29T02:46:57+00:00: Support the 5B fun inpaint model. (#9614) - https://github.com/comfyanonymous/ComfyUI/commit/c7bb3e2bceaad7accd52c23d22b97a1b6808304b __auto-added__
- 2025-08-29T08:12:00+00:00: Trim audio to video when saving video. (#9617) - https://github.com/comfyanonymous/ComfyUI/commit/15aa9222c4d1fc74f5190d7c7e56ef986d0d7146 __auto-added__
- 2025-08-29T10:03:41+00:00: ComfyUI v0.3.55 - https://github.com/comfyanonymous/ComfyUI/commit/a86aaa430183068e2a264495c802c81d05eb350a __auto-added__
- 2025-08-29T10:03:41+00:00: v0.3.55 - https://github.com/comfyanonymous/ComfyUI/releases/tag/v0.3.55 __auto-added__
- 2025-08-29T12:40:30+00:00: v0.4.68 - https://github.com/Comfy-Org/desktop/releases/tag/v0.4.68 __auto-added__
- 2025-08-29T14:20:41+00:00: Wan2.2 S2V in ComfyUI: Audio-Driven Video Generation from Static Images - https://blog.comfy.org/p/wan22-s2v-in-comfyui-audio-driven __auto-added__
- 2025-08-30T03:06:04+00:00: Lower ram usage on windows. (#9628) - https://github.com/comfyanonymous/ComfyUI/commit/885015eecf649d6e49e1ade68e4475b434517b82 __auto-added__
- 2025-08-30T10:31:19+00:00: ComfyUI version 0.3.56 - https://github.com/comfyanonymous/ComfyUI/commit/4449e147692366ac8b9bd3b8834c771bc81e91ac __auto-added__
- 2025-08-30T10:31:19+00:00: v0.3.56 - https://github.com/comfyanonymous/ComfyUI/releases/tag/v0.3.56 __auto-added__
- 2025-08-30T12:22:36+00:00: v0.4.69 - https://github.com/Comfy-Org/desktop/releases/tag/v0.4.69 __auto-added__
- 2025-08-31T03:21:58+00:00: convert Primitive nodes to V3 schema (#9372) - https://github.com/comfyanonymous/ComfyUI/commit/fe442fac2eccd0cc66999b48d3c518623cafe4fc __auto-added__
- 2025-08-31T04:01:45+00:00: SEEDS: update noise decomposition and refactor (#9633) - https://github.com/comfyanonymous/ComfyUI/commit/32a627bf1feadb83abba97906a27978b927abd33 __auto-added__
- 2025-08-31T05:32:10+00:00: Probably not necessary anymore. (#9646) - https://github.com/comfyanonymous/ComfyUI/commit/9b151559721ff6c8d93150f3d8a53259a23911cd __auto-added__
- 2025-09-01T22:54:02+00:00: Implement the USO subject identity lora. (#9674) - https://github.com/comfyanonymous/ComfyUI/commit/27e067ce505c102fd0f2be0f1242016c59a6816f __auto-added__
- 2025-09-02T00:33:50+00:00: Enable Convolution AutoTuning (#9301) - https://github.com/comfyanonymous/ComfyUI/commit/e2d1e5dad98dbbcf505703ea8663f20101e6570a __auto-added__
- 2025-09-02T19:36:22+00:00: USO style reference. (#9677) - https://github.com/comfyanonymous/ComfyUI/commit/3412d53b1d69e4dfedf7e86c3092cea085094053 __auto-added__
- 2025-09-02T20:12:07+00:00: uso -> uxo/uno as requested.  (#9688) - https://github.com/comfyanonymous/ComfyUI/commit/e3018c2a5aeb99f0c5b595621949a451686ce55a __auto-added__
- 2025-09-02T23:41:10+00:00: Accept prompt_id in interrupt handler (#9607) - https://github.com/comfyanonymous/ComfyUI/commit/464ba1d6140eda6a0173703ac00c69f7fddab6ba __auto-added__
- 2025-09-03T00:06:41+00:00: Update template to 0.1.73 (#9686) - https://github.com/comfyanonymous/ComfyUI/commit/4f5812b93712e0f52ae8fe80a89e8b5e7d0fa309 __auto-added__
- 2025-09-03T02:17:36+00:00: v1.26.8 - https://github.com/Comfy-Org/ComfyUI_frontend/releases/tag/v1.26.8 __auto-added__
- 2025-09-03T02:25:25+00:00: "Falling": The Comfy Challenge #2 Montage - https://blog.comfy.org/p/falling-the-comfy-challenge-2-montage __auto-added__
- 2025-09-03T18:01:07+00:00: v1.26.9 - https://github.com/Comfy-Org/ComfyUI_frontend/releases/tag/v1.26.9 __auto-added__
- 2025-09-03T20:18:27+00:00: [V3] convert Runway API nodes to the V3 schema (#9487) - https://github.com/comfyanonymous/ComfyUI/commit/22da0a83e9a251ca16b9753bf808bfa9f4b023d8 __auto-added__
- 2025-09-03T22:43:29+00:00: Update comment in api example. (#9708) - https://github.com/comfyanonymous/ComfyUI/commit/4368d8f87f580f526e8b2bc43bf0ac88e2b67033 __auto-added__
- 2025-09-04T02:20:13+00:00: Fix potential rope issue. (#9710) - https://github.com/comfyanonymous/ComfyUI/commit/72855db715096bc378817b1aaffcf232fdc39659 __auto-added__
- 2025-09-04T06:15:57+00:00: ComfyUI 0.3.57 - https://github.com/comfyanonymous/ComfyUI/commit/b0338e930bbc1f9d01f005f224573d5994732932 __auto-added__
- 2025-09-04T06:15:57+00:00: v0.3.57 - https://github.com/comfyanonymous/ComfyUI/releases/tag/v0.3.57 __auto-added__
- 2025-09-04T07:19:06+00:00: v1.27.0 - https://github.com/Comfy-Org/ComfyUI_frontend/releases/tag/v1.27.0 __auto-added__
- 2025-09-04T07:24:23+00:00: v0.4.70 - https://github.com/Comfy-Org/desktop/releases/tag/v0.4.70 __auto-added__
- 2025-09-04T10:05:21+00:00: 5.4.1 - https://github.com/runpod-workers/worker-comfyui/releases/tag/5.4.1 __auto-added__
- 2025-09-04T14:01:28+00:00: USO Unified Style and Subject-Driven Generation Now Available in ComfyUI - https://blog.comfy.org/p/uso-available-in-comfyui __auto-added__
- 2025-09-04T23:13:28+00:00: Fix progress update crossover between users (#9706) - https://github.com/comfyanonymous/ComfyUI/commit/a9f1bb10a52ce08a3f21e6fc562554671c85c3d5 __auto-added__
- 2025-09-05T00:39:02+00:00: Some changes to the previous hunyuan PR. (#9725) - https://github.com/comfyanonymous/ComfyUI/commit/c9ebe70072213a875ffbe40cc1b36820b2005211 __auto-added__
- 2025-09-05T06:39:57+00:00: v1.27.1 - https://github.com/Comfy-Org/ComfyUI_frontend/releases/tag/v1.27.1 __auto-added__
- 2025-09-05T18:32:25+00:00: fix: add cache headers for images  (#9560) - https://github.com/comfyanonymous/ComfyUI/commit/3493b9cb1f9a9a66b1b86ed908cf87bc382b647a __auto-added__
- 2025-09-05T18:57:35+00:00: Fix lowvram issues with hunyuan3d 2.1 (#9735) - https://github.com/comfyanonymous/ComfyUI/commit/2ee7879a0bdbf507bfd26f8b36eca2fef147c29d __auto-added__
- 2025-09-06T05:05:05+00:00: Print all fast options in --help (#9737) - https://github.com/comfyanonymous/ComfyUI/commit/ea6cdd2631fbca6ed81b95796150c32c9a029f0d __auto-added__
- 2025-09-07T03:25:22+00:00: Enable bf16 VAE on RDNA4. (#9746) - https://github.com/comfyanonymous/ComfyUI/commit/27a0fcccc376fef6f035ed97664db8aa7e2e6117 __auto-added__
- 🔥 2025-09-07T04:29:38+00:00: Don't enable pytorch attention on AMD if triton isn't available. (#9747) - https://github.com/comfyanonymous/ComfyUI/commit/bcbd7884e3af5ee8b6ab848da2a3123f247d6114 __priority-auto-added__
- 2025-09-07T07:42:34+00:00: v1.27.2 - https://github.com/Comfy-Org/ComfyUI_frontend/releases/tag/v1.27.2 __auto-added__
- 2025-09-08T01:16:29+00:00: Fix amd_min_version crash when cpu device. (#9754) - https://github.com/comfyanonymous/ComfyUI/commit/fb763d43332aaf15e96350cf1c25e2a1927423f1 __auto-added__
- 2025-09-08T19:08:18+00:00: Add explicit casting in apply_rope for Qwen VL (#9759) - https://github.com/comfyanonymous/ComfyUI/commit/97652d26b81f83fc9a3675be55ede7762fafb7bd __auto-added__
- 2025-09-08T21:30:26+00:00: Support qwen inpaint controlnet. (#9772) - https://github.com/comfyanonymous/ComfyUI/commit/103a12cb668303f197b22f52bb2981bb1539beea __auto-added__
- 2025-09-09T18:40:29+00:00: add ByteDance video API nodes (#9712) - https://github.com/comfyanonymous/ComfyUI/commit/f73b176abd6b3e3b587b668fa6748107deef311c __auto-added__
- 2025-09-09T22:09:56+00:00: Small refactor of some vae code. (#9787) - https://github.com/comfyanonymous/ComfyUI/commit/b288fb0db88281532d813d4fb83f715f88b54ffc __auto-added__
- 2025-09-09T22:30:52+00:00: "Latent Reforge": Comfy Challenge #3 Montage - https://blog.comfy.org/p/latent-reforge-comfy-challenge-3 __auto-added__
- 2025-09-10T01:33:36+00:00: Change validate_inputs' output typehint to 'bool | str' and update do… - https://github.com/comfyanonymous/ComfyUI/commit/206595f854c67538d5921d36326acbfeb69c5ac2 __auto-added__
- 🔥 2025-09-10T04:23:47+00:00: Fix issue on old torch. (#9791) - https://github.com/comfyanonymous/ComfyUI/commit/5c33872e2f355e51adf212d5b5c83815b7fe77b0 __priority-auto-added__
- 2025-09-10T06:15:34+00:00: Fix lowvram issue with hunyuan image vae. (#9794) - https://github.com/comfyanonymous/ComfyUI/commit/543888d3d84a6ec4c4273838d5179845840e3226 __auto-added__
- 2025-09-10T09:06:47+00:00: add StabilityAudio API nodes (#9749) - https://github.com/comfyanonymous/ComfyUI/commit/de44b95db6c7ef107f26e7edf30748b608afaa48 __auto-added__
- 2025-09-10T14:51:02+00:00: ComfyUI version v0.3.58 - https://github.com/comfyanonymous/ComfyUI/commit/8d7c930246bd33c32eb957b01ab0d364af6e81c0 __auto-added__
- 2025-09-10T14:51:02+00:00: v0.3.58 - https://github.com/comfyanonymous/ComfyUI/releases/tag/v0.3.58 __auto-added__
- 2025-09-10T14:49:07+00:00: Stable Audio 2.5 is now in ComfyUI! - https://blog.comfy.org/p/stable-audio-25-is-now-in-comfyui __auto-added__
- 2025-09-10T16:29:58+00:00: v0.4.71 - https://github.com/Comfy-Org/desktop/releases/tag/v0.4.71 __auto-added__
- 2025-09-10T21:16:41+00:00: Update template to 0.1.78 (#9806) - https://github.com/comfyanonymous/ComfyUI/commit/df34f1549a431c85a6326e87075a206228697cde __auto-added__
- 2025-09-10T21:25:41+00:00: ComfyUI version 0.3.59 - https://github.com/comfyanonymous/ComfyUI/commit/72212fef660bcd7d9702fa52011d089c027a64d8 __auto-added__
- 2025-09-10T21:25:41+00:00: v0.3.59 - https://github.com/comfyanonymous/ComfyUI/releases/tag/v0.3.59 __auto-added__
- 2025-09-10T21:44:56+00:00: Seedream 4.0 Now Available in ComfyUI! - https://blog.comfy.org/p/seedream-40-now-available-in-comfyui __auto-added__
- 2025-09-10T22:21:52+00:00: v0.4.72 - https://github.com/Comfy-Org/desktop/releases/tag/v0.4.72 __auto-added__
- 2025-09-11T03:17:34+00:00: Support hunyuan image distilled model. (#9807) - https://github.com/comfyanonymous/ComfyUI/commit/e01e99d075852b94e93f27ea64ab862a49a7d2cc __auto-added__
- 2025-09-11T08:49:47+00:00: v1.26.10 - https://github.com/Comfy-Org/ComfyUI_frontend/releases/tag/v1.26.10 __auto-added__
- 2025-09-11T18:59:26+00:00: Update template to 0.1.81 (#9811) - https://github.com/comfyanonymous/ComfyUI/commit/df6850fae8a75126cb7a645e38d58cebcfd51096 __auto-added__
- 2025-09-11T20:45:57+00:00: v1.27.3 - https://github.com/Comfy-Org/ComfyUI_frontend/releases/tag/v1.27.3 __auto-added__
- 2025-09-11T23:33:02+00:00: Fast preview for hunyuan image. (#9814) - https://github.com/comfyanonymous/ComfyUI/commit/18de0b28305fd8bf002d74e91c0630bd76b01d6b __auto-added__
- 2025-09-12T04:46:01+00:00: Bump frontend to 1.26.11 (#9809) - https://github.com/comfyanonymous/ComfyUI/commit/d6b977b2e680e98ad18a37ee13783da4f30e15f4 __auto-added__
- 2025-09-12T20:03:08+00:00: Add noise augmentation to hunyuan image refiner. (#9831) - https://github.com/comfyanonymous/ComfyUI/commit/fd2b820ec28e9575877dc6c51949b2d28dc78894 __auto-added__
- 2025-09-12T20:35:34+00:00: Fix hunyuan refiner blownout colors at noise aug less than 0.25 (#9832) - https://github.com/comfyanonymous/ComfyUI/commit/e600520f8aa583c79caa286a8d7d584edc3d059b __auto-added__
- 2025-09-12T20:40:12+00:00: Set default hunyuan refiner shift to 4.0 (#9833) - https://github.com/comfyanonymous/ComfyUI/commit/7757d5a657cbe9b22d1f3538ee0bc5387d3f5459 __auto-added__
- 2025-09-12T21:29:03+00:00: add kling-v2-1 model to the KlingStartEndFrame node (#9630) - https://github.com/comfyanonymous/ComfyUI/commit/0aa074a420c450fd7793d83c6f8d66009a1ca2a2 __auto-added__
- 2025-09-12T21:41:26+00:00: convert Moonvalley API nodes to the V3 schema (#9698) - https://github.com/comfyanonymous/ComfyUI/commit/581bae2af30b0839a39734bd97006c4009f9d70a __auto-added__
- 2025-09-12T22:07:38+00:00: Enable Runtime Selection of Attention Functions (#9639) - https://github.com/comfyanonymous/ComfyUI/commit/d7f40442f91a02946cab7445c6204bf154b1e86f __auto-added__
- 2025-09-12T23:46:46+00:00: Hunyuan refiner vae now works with tiled. (#9836) - https://github.com/comfyanonymous/ComfyUI/commit/a3b04de7004cc19dee9364bd71e62bab05475810 __auto-added__
- 2025-09-13T01:57:04+00:00: Cleanup. (#9838) - https://github.com/comfyanonymous/ComfyUI/commit/29bf807b0e2d89402d555d08bd8e9df15e636f0c __auto-added__
- 2025-09-13T20:59:19+00:00: Remove single quote pattern to avoid wrong matches (#9842) - https://github.com/comfyanonymous/ComfyUI/commit/e5e70636e7b7b54695220a88ab036c1607959736 __auto-added__
- 2025-09-13T22:03:34+00:00: Changes to the previous radiance commit. (#9851) - https://github.com/comfyanonymous/ComfyUI/commit/80b7c9455bf7afba7a9e95a1eb76b172408ab56c __auto-added__
- 2025-09-14T01:34:21+00:00: Make ModuleNotFoundError ImportError instead (#9850) - https://github.com/comfyanonymous/ComfyUI/commit/f228367c5e3906de194968fa9b6fbe7aa9987bfa __auto-added__
- 2025-09-14T08:05:38+00:00: Add that hunyuan image is supported to readme. (#9857) - https://github.com/comfyanonymous/ComfyUI/commit/4f1f26ac6c11b803bbc83cb347178e2f9b5e421b __auto-added__
- 2025-09-15T15:05:58+00:00: Comfy Cloud - https://blog.comfy.org/p/comfy-cloud __auto-added__
- 2025-09-15T18:55:33+00:00: v1.27.4 - https://github.com/Comfy-Org/ComfyUI_frontend/releases/tag/v1.27.4 __auto-added__
- 2025-09-15T22:10:55+00:00: Support the omnigen2 umo lora. (#9886) - https://github.com/comfyanonymous/ComfyUI/commit/47a9cde5d3045c42f20baafb9855fb96959124f0 __auto-added__
- 2025-09-16T00:05:03+00:00: Fix depending on asserts to raise an exception in BatchedBrownianTree… - https://github.com/comfyanonymous/ComfyUI/commit/1a85483da159f2800407ae5a8a45eb0d88ffce2d __auto-added__
- 2025-09-16T05:19:50+00:00: Add encoder part of whisper large v3 as an audio encoder model. (#9894) - https://github.com/comfyanonymous/ComfyUI/commit/a39ac59c3e3fddc8b278899814f0bd5371abb11f __auto-added__
- 2025-09-16T15:34:49+00:00: Comfy Raises $17M Funding - https://blog.comfy.org/p/comfy-raises-17m-funding __auto-added__
- 2025-09-16T23:21:14+00:00: Reduce Peak WAN inference VRAM usage (#9898) - https://github.com/comfyanonymous/ComfyUI/commit/e42682b24ef033a93001ba27cc5c5aa461a61d8d __auto-added__
- 2025-09-17T03:44:03+00:00: v1.27.5 - https://github.com/Comfy-Org/ComfyUI_frontend/releases/tag/v1.27.5 __auto-added__
- 2025-09-17T04:12:48+00:00: Support the HuMo model. (#9903) - https://github.com/comfyanonymous/ComfyUI/commit/9288c78fc5fae74d3fa7787736dea442e996303f __auto-added__
- 2025-09-17T22:39:24+00:00: Support the HuMo 17B model. (#9912) - https://github.com/comfyanonymous/ComfyUI/commit/dd611a7700956f45f393dee32fb8505de176dc66 __auto-added__
- 2025-09-18T15:00:55+00:00: "Pose Alchemy": Comfy Challenge #4 Montage & #5 Reveal - https://blog.comfy.org/p/pose-alchemy-comfy-challenge-4-montage __auto-added__
- 2025-09-18T21:15:46+00:00: v1.28.0 - https://github.com/Comfy-Org/ComfyUI_frontend/releases/tag/v1.28.0 __auto-added__
- 2025-09-18T23:54:16+00:00: Do padding of audio embed in model for humo for more flexibility. (#9… - https://github.com/comfyanonymous/ComfyUI/commit/24b0fce099c56d18ceb1f4f6b9455fee55e154ce __auto-added__
- 2025-09-19T03:19:22+00:00: v1.26.13 - https://github.com/Comfy-Org/ComfyUI_frontend/releases/tag/v1.26.13 __auto-added__
- 2025-09-19T07:07:17+00:00: Basic WIP support for the wan animate model. (#9939) - https://github.com/comfyanonymous/ComfyUI/commit/dc95b6acc0ef4962460592d417db4024f7160586 __auto-added__
- 2025-09-19T20:04:51+00:00: fix(seedream4): add flag to ignore error on partial success (#9952) - https://github.com/comfyanonymous/ComfyUI/commit/852704c81a652cc53fbe53c5f47dea0e50d0534e __auto-added__
- 2025-09-19T22:48:56+00:00: Update WanAnimateToVideo to more easily extend videos. (#9959) - https://github.com/comfyanonymous/ComfyUI/commit/e8df53b764c7dfce1a9235f6ee70a17cfdece3ff __auto-added__
- 2025-09-20T06:24:10+00:00: Add inputs for character replacement to the WanAnimateToVideo node. (… - https://github.com/comfyanonymous/ComfyUI/commit/66241cef31f21247ec8b450d699250fd83b3ff7c __auto-added__
- 2025-09-21T02:09:35+00:00: Lower wan memory estimation value a bit. (#9964) - https://github.com/comfyanonymous/ComfyUI/commit/d1d9eb94b1096c9b3f963bf152bd6b9cd330c3a4 __auto-added__
- 2025-09-21T23:48:31+00:00: Set some wan nodes as no longer experimental. (#9976) - https://github.com/comfyanonymous/ComfyUI/commit/27bc181c49249f11da2d8a14f84f3bdb58a0615f __auto-added__
- 2025-09-22T20:04:04+00:00: v0.4.73 - https://github.com/Comfy-Org/desktop/releases/tag/v0.4.73 __auto-added__
- 2025-09-22T20:49:48+00:00: Support for qwen edit plus model. Use the new TextEncodeQwenImageEdit… - https://github.com/comfyanonymous/ComfyUI/commit/1fee8827cb8160c85d96c375413ac590311525dc __auto-added__
- 2025-09-22T21:12:32+00:00: add offset param (#9977) - https://github.com/comfyanonymous/ComfyUI/commit/e3206351b07852f2127a56abd898ee77f7f4c25f __auto-added__
- 2025-09-22T21:26:58+00:00: Fix bug with WanAnimateToVideo node. (#9988) - https://github.com/comfyanonymous/ComfyUI/commit/8a5ac527e60fcd48ec228d309d49ab28ac79def8 __auto-added__
- 2025-09-22T21:34:33+00:00: Fix bug with WanAnimateToVideo. (#9990) - https://github.com/comfyanonymous/ComfyUI/commit/707b2638ecd82360c0a67e1d86cc4fdeae218d03 __auto-added__
- 2025-09-23T01:38:19+00:00: v1.28.1 - https://github.com/Comfy-Org/ComfyUI_frontend/releases/tag/v1.28.1 __auto-added__
- 2025-09-23T15:22:35+00:00: update template to 0.1.86 (#9998) - https://github.com/comfyanonymous/ComfyUI/commit/145b0e4f79b5d9e815bb781ba29ccd057bb52dab __auto-added__
- 2025-09-23T15:36:47+00:00: feat(api-nodes): add wan t2i, t2v, i2v nodes (#9996) - https://github.com/comfyanonymous/ComfyUI/commit/e8087907995497c6971ee64bd5fa02cb49c1eda6 __auto-added__
- 2025-09-23T15:50:33+00:00: ComfyUI version 0.3.60 - https://github.com/comfyanonymous/ComfyUI/commit/b8730510db30c8858e1e5d8e126ef19eac395560 __auto-added__
- 2025-09-23T15:50:33+00:00: v0.3.60 - https://github.com/comfyanonymous/ComfyUI/releases/tag/v0.3.60 __auto-added__
- 2025-09-23T17:33:50+00:00: v0.4.74 - https://github.com/Comfy-Org/desktop/releases/tag/v0.4.74 __auto-added__
- 2025-09-23T19:55:25+00:00: WAN2.2 Animate & Qwen-Image-Edit 2509 Native Support in ComfyUI - https://blog.comfy.org/p/wan22-animate-and-qwen-image-edit-2509 __auto-added__
- 2025-09-24T01:44:23+00:00: v1.26.15 - https://github.com/Comfy-Org/ComfyUI_frontend/releases/tag/v1.26.15 __auto-added__
- 2025-09-24T03:44:07+00:00: Wan 2.5 (preview) API Nodes in ComfyUI - https://blog.comfy.org/p/wan-25-preview-api-nodes-in-comfyui __auto-added__
- 2025-09-24T18:05:37+00:00: Rodin3D - add [Rodin3D Gen-2 generate] api-node (#9994) - https://github.com/comfyanonymous/ComfyUI/commit/341b4adefd308cbcf82c07effc255f2770b3b3e2 __auto-added__
- 2025-09-24T22:59:29+00:00: Add new audio nodes (#9908) - https://github.com/comfyanonymous/ComfyUI/commit/fd79d32f38fd24adca5a6e8214f05050f287c9db __auto-added__
- 2025-09-25T00:09:42+00:00: Fix issue with .view() in HuMo. (#10014) - https://github.com/comfyanonymous/ComfyUI/commit/fccab99ec0fcd13e80fa59bc73bccff31f9450ca __auto-added__
- 2025-09-25T02:35:12+00:00: Fix memory leak by properly detaching model finalizer (#9979) - https://github.com/comfyanonymous/ComfyUI/commit/c8d2117f02bcad6d8316ffd8273bdc27adf83b44 __auto-added__
- 2025-09-25T02:23:05+00:00: v1.28.2 - https://github.com/Comfy-Org/ComfyUI_frontend/releases/tag/v1.28.2 __auto-added__
- 2025-09-25T15:03:22+00:00: "Heartbeat": Comfy Challenge #6 X Wan Muse - https://blog.comfy.org/p/comfy-challenge-x-wan __auto-added__
- 2025-09-25T21:20:13+00:00: Make LatentCompositeMasked work with basic video latents. (#10023) - https://github.com/comfyanonymous/ComfyUI/commit/ce4cb2389c8ce63cf8735f200b8672a2c1be0950 __auto-added__
- 2025-09-26T04:06:20+00:00: HuMo & Chroma1-Radiance Native Support in ComfyUI - https://blog.comfy.org/p/humo-and-chroma1-radiance-support __auto-added__
- 2025-09-26T18:12:43+00:00: Fix the failing unit test. (#10037) - https://github.com/comfyanonymous/ComfyUI/commit/2b7f9a8196304badb5fe58e5c734e4b182ad0fdf __auto-added__
- 2025-09-26T21:08:16+00:00: Add @kosinkadink as code owner (#10041) - https://github.com/comfyanonymous/ComfyUI/commit/c4a46e943c12c7f3f6ac72f8fb51caad514ec9b6 __auto-added__
- 2025-09-26T21:15:44+00:00: convert CLIPTextEncodeSDXL nodes to V3 schema (#9716) - https://github.com/comfyanonymous/ComfyUI/commit/cd66d72b464fd9d344baa426b50a5f0e5e512f99 __auto-added__
- 2025-09-26T22:34:17+00:00: Don't add template to qwen2.5vl when template is in prompt. (#10043) - https://github.com/comfyanonymous/ComfyUI/commit/1e098d61327e1c02c1a47b2626514474aa8e3c7e __auto-added__
- 2025-09-27T02:55:03+00:00: Add 'input_cond' and 'input_uncond' to the args dictionary passed int… - https://github.com/comfyanonymous/ComfyUI/commit/196954ab8c55bc4ac48113686a57ce250677c7b5 __auto-added__
- 2025-09-27T04:29:13+00:00: Add workflow templates version tracking to system_stats (#9089) - https://github.com/comfyanonymous/ComfyUI/commit/255572188f79e5c58fa997bf73529021129459a9 __auto-added__
- 2025-09-27T06:13:05+00:00: convert nodes_hidream.py to V3 schema (#9946) - https://github.com/comfyanonymous/ComfyUI/commit/a9cf1cd249773632949bec2262f921f64378127f __auto-added__
- 2025-09-27T09:28:11+00:00: convert nodes_luma.py to V3 schema (#10030) - https://github.com/comfyanonymous/ComfyUI/commit/bcfd80dd79ccfa77a7da69380795fbb55b65b1ba __auto-added__
- 2025-09-27T09:36:43+00:00: convert nodes_photomaker.py to V3 schema (#10017) - https://github.com/comfyanonymous/ComfyUI/commit/7eca95657cf7a70c15d598c969b890a164a300a1 __auto-added__
- 2025-09-27T19:25:35+00:00: convert nodes_qwen.py to V3 schema (#10049) - https://github.com/comfyanonymous/ComfyUI/commit/160698eb418269d64fbbe8c34db27a4d1ddb0540 __auto-added__
- 2025-09-27T22:07:53+00:00: v1.28.3 - https://github.com/Comfy-Org/ComfyUI_frontend/releases/tag/v1.28.3 __auto-added__
- 2025-09-27T22:14:16+00:00: Reduce Peak WAN inference VRAM usage - part II (#10062) - https://github.com/comfyanonymous/ComfyUI/commit/653ceab4148a9fbc050ebceb674acef760792b77 __auto-added__
- 2025-09-28T00:28:49+00:00: Improvements to the stable release workflow. (#10065) - https://github.com/comfyanonymous/ComfyUI/commit/40ae495ddcbc04846e91ccad3e844bb34d98c6fd __auto-added__
- 2025-09-28T02:36:02+00:00: feat: ComfyUI can be run on the specified Ascend NPU (#9663) - https://github.com/comfyanonymous/ComfyUI/commit/1364548c721a466adcdc60e49ee291b0d4255245 __auto-added__
- 2025-09-28T02:43:25+00:00: Fix stable workflow creating multiple draft releases. (#10067) - https://github.com/comfyanonymous/ComfyUI/commit/555f902fc1ed20e98201f9102172f0fc190c2c42 __auto-added__
- 🔥 2025-09-28T17:41:32+00:00: Update command to install latest nighly pytorch. (#10085) - https://github.com/comfyanonymous/ComfyUI/commit/b60dc316272ba139e06b8a7b2f5f5b622c9afe20 __priority-auto-added__
- 2025-09-29T19:05:28+00:00: convert nodes_perpneg.py to V3 schema (#10081) - https://github.com/comfyanonymous/ComfyUI/commit/041b8824f50e01803637d5e83c3f4edaf628f43a __auto-added__
- 2025-09-29T19:16:02+00:00: dont cache new locale entry points (#10101) - https://github.com/comfyanonymous/ComfyUI/commit/ed0f4a609b5e6821f97db5cb1715068c25f78e7b __auto-added__
- 2025-09-29T19:35:51+00:00: convert nodes_mahiro.py to V3 schema (#10070) - https://github.com/comfyanonymous/ComfyUI/commit/8accf50908094d9cd39168981fa5394274d25491 __auto-added__
- 🔥 2025-09-29T21:27:52+00:00: Add action to create cached deps with manually specified torch. (#10102) - https://github.com/comfyanonymous/ComfyUI/commit/7f38e4c538de2fa38d0539c18577cdd0e5d251c2 __priority-auto-added__
- 2025-09-29T23:08:42+00:00: Make the final release test optional in the stable release action. (#… - https://github.com/comfyanonymous/ComfyUI/commit/1673ace19b9d63a8dc0d388aafdb54abf2497892 __auto-added__
- 2025-09-30T00:37:51+00:00: Make stable release workflow callable. (#10108) - https://github.com/comfyanonymous/ComfyUI/commit/447884b65740d9f4160ef13d55adb49ca111140e __auto-added__
- 2025-09-30T03:04:42+00:00: ComfyUI version 0.3.61 - https://github.com/comfyanonymous/ComfyUI/commit/977a4ed8c55ade53d0d6cfe1fe8a6396ee35a2ec __auto-added__
- 2025-09-30T03:04:42+00:00: v0.3.61 - https://github.com/comfyanonymous/ComfyUI/releases/tag/v0.3.61 __auto-added__
- 2025-09-30T03:11:37+00:00: Workflow permission fix. (#10110) - https://github.com/comfyanonymous/ComfyUI/commit/6e079abc3a3fc0fb98e2a0848877874151310ed1 __auto-added__
- 2025-09-30T04:02:56+00:00: v0.4.75 - https://github.com/Comfy-Org/desktop/releases/tag/v0.4.75 __auto-added__
- 2025-09-30T16:17:49+00:00: Add new portable links to readme. (#10112) - https://github.com/comfyanonymous/ComfyUI/commit/f48d7230de2f7b10fe8bfda3d7f53241d19c7266 __auto-added__
- 2025-09-30T17:21:47+00:00: fix(Rodin3D-Gen2): missing "task_uuid" parameter (#10128) - https://github.com/comfyanonymous/ComfyUI/commit/631b9ae861bf8bdd3c538da232e4c8938448e59d __auto-added__
- 2025-09-30T17:43:41+00:00: enable Seedance Pro model in the FirstLastFrame node (#10120) - https://github.com/comfyanonymous/ComfyUI/commit/b682a73c55a6434fdd9293d45ace969597f8ad65 __auto-added__
- 2025-09-30T19:12:07+00:00: ComfyUI version 0.3.62. - https://github.com/comfyanonymous/ComfyUI/commit/bab8ba20bf47d985d6b1d73627c2add76bd4e716 __auto-added__
- 2025-09-30T19:12:07+00:00: v0.3.62 - https://github.com/comfyanonymous/ComfyUI/releases/tag/v0.3.62 __auto-added__
- 2025-09-30T20:00:10+00:00: v1.27.7 - https://github.com/Comfy-Org/ComfyUI_frontend/releases/tag/v1.27.7 __auto-added__
- 2025-09-30T20:06:07+00:00: v0.4.76 - https://github.com/Comfy-Org/desktop/releases/tag/v0.4.76 __auto-added__
- 2025-10-01T04:42:57+00:00: v1.28.4 - https://github.com/Comfy-Org/ComfyUI_frontend/releases/tag/v1.28.4 __auto-added__
- 2025-10-01T05:12:32+00:00: Bump frontend to 1.27.7 (#10133) - https://github.com/comfyanonymous/ComfyUI/commit/c4a8cf60ab5d6eaf052b7a08f5ee97104acf7a2f __auto-added__
- 2025-10-01T06:00:22+00:00: convert nodes_audio_encoder.py to V3 schema (#10123) - https://github.com/comfyanonymous/ComfyUI/commit/638097829d2352a1c78ab4fbb1e028d1e7cff012 __auto-added__
- 2025-10-01T19:20:30+00:00: convert nodes_ip2p.pt to V3 schema (#10097) - https://github.com/comfyanonymous/ComfyUI/commit/e4f99b479a19730bea890567129f4032b4dd4787 __auto-added__
- 2025-10-01T19:26:11+00:00: Comfy Challenge #6: Heartbeat - https://blog.comfy.org/p/comfy-challenge-6-heartbeat __auto-added__
- 2025-10-01T21:19:13+00:00: Support the new hunyuan vae. (#10150) - https://github.com/comfyanonymous/ComfyUI/commit/a6f83a4a1a70d720c16d66feb5d87fee5998acdf __auto-added__
- 2025-10-01T21:59:07+00:00: feat: Add Epsilon Scaling node for exposure bias correction (#10132) - https://github.com/comfyanonymous/ComfyUI/commit/bb32d4ec3141333df26fcdaee0c3c08e41b7b249 __auto-added__
- 2025-10-01T22:42:16+00:00: WAN: Fix cache VRAM leak on error (#10141) - https://github.com/comfyanonymous/ComfyUI/commit/4965c0e2acf39d84e82cb63dd6cc4400299d0a61 __auto-added__
- 2025-10-02T04:33:05+00:00: Add a .bat to the AMD portable to disable smart memory. (#10153) - https://github.com/comfyanonymous/ComfyUI/commit/0e9d1724be327c79ba86159d868f0b57adb8c384 __auto-added__
- 2025-10-02T20:53:00+00:00: convert nodes_morphology.py to V3 schema (#10159) - https://github.com/comfyanonymous/ComfyUI/commit/8f4ee9984c0c3864290e4fea81cfea2ba281717d __auto-added__
- 🔥 2025-10-02T21:57:15+00:00: Turn on TORCH_ROCM_AOTRITON_ENABLE_EXPERIMENTAL by default. (#10168) - https://github.com/comfyanonymous/ComfyUI/commit/e9364ee279f65d0546fea1796c3cd2e0b7e1965f __priority-auto-added__
- 2025-10-02T22:20:29+00:00: update example_node to use V3 schema (#9723) - https://github.com/comfyanonymous/ComfyUI/commit/1395bce9f707e52ec613eeaa87ea690518cfe0a8 __auto-added__
- 2025-10-02T23:14:28+00:00: feat(linter, api-nodes): add pylint for comfy_api_nodes folder (#10157) - https://github.com/comfyanonymous/ComfyUI/commit/4ffea0e864275301329ddb5ecc3fbc7211d7a802 __auto-added__
- 2025-10-03T14:52:17+00:00: v1.28.5 - https://github.com/Comfy-Org/ComfyUI_frontend/releases/tag/v1.28.5 __auto-added__
- 2025-10-03T15:02:57+00:00: Frame Control Unlocked: Seedance Pro in ComfyUI - https://blog.comfy.org/p/frame-control-unlocked-seedance-pro __auto-added__
- 🔥 2025-10-03T18:43:54+00:00: convert nodes_torch_compile.py to V3 schema (#10173) - https://github.com/comfyanonymous/ComfyUI/commit/3e68bc342cd60b909b4117c1b68a3afc62ef875c __priority-auto-added__
- 2025-10-03T18:50:38+00:00: convert nodes_tomesd.py to V3 schema (#10180) - https://github.com/comfyanonymous/ComfyUI/commit/5c8e986e273d8af8b976fddbaed726e8278cf1fe __auto-added__
- 2025-10-03T20:24:42+00:00: convert nodes_edit_model.py to V3 schema (#10147) - https://github.com/comfyanonymous/ComfyUI/commit/4614ee09ca1aaca7ee8067d6c5c30695582326ff __auto-added__
- 2025-10-03T21:32:19+00:00: Fix type annotation syntax in MotionEncoder_tc __init__ (#10186) - https://github.com/comfyanonymous/ComfyUI/commit/93d859cfaaad150c2a1e5e54c8f14765fa79ecb5 __auto-added__
- 2025-10-03T22:22:43+00:00: Update amd nightly command in readme. (#10189) - https://github.com/comfyanonymous/ComfyUI/commit/08726b64fe767f47bf074a05bedd6db45314c4c9 __auto-added__
- 🔥 2025-10-04T03:37:43+00:00: Add instructions to install nightly AMD pytorch for windows. (#10190) - https://github.com/comfyanonymous/ComfyUI/commit/bbd683098e7d18700f025b2f0a4f6a44a3176602 __priority-auto-added__
- 2025-10-04T19:33:48+00:00: convert nodes_stable3d.py to V3 schema (#10204) - https://github.com/comfyanonymous/ComfyUI/commit/b1fa1922df597af759150f4e26ecb276c9753ee4 __auto-added__
- 🔥 2025-10-05T02:05:05+00:00: Remove soundfile dependency. No more torchaudio load or save. (#10210) - https://github.com/comfyanonymous/ComfyUI/commit/caf07331ff1b20f4104b9693ed244d6e22f80b5a __priority-auto-added__
- 2025-10-05T06:34:18+00:00: fix(api-nodes): disable "std" mode for Kling2.5-turbo (#10212) - https://github.com/comfyanonymous/ComfyUI/commit/187f43696dd58f252075d2e3c6873706eb6b5fa1 __auto-added__
- 2025-10-05T19:41:19+00:00: Remove useless code. (#10223) - https://github.com/comfyanonymous/ComfyUI/commit/195e0b063950f585fe584c5ce7b0b689f8d20ff8 __auto-added__
- 2025-10-06T04:55:59+00:00: v1.28.6 - https://github.com/Comfy-Org/ComfyUI_frontend/releases/tag/v1.28.6 __auto-added__
- 2025-10-06T17:57:00+00:00: Update template to 0.1.93 (#10235) - https://github.com/comfyanonymous/ComfyUI/commit/7326e46deeab97219cad32d0624991f9ffea4fe5 __auto-added__
- 2025-10-06T18:49:04+00:00: ComfyUI version 0.3.63 - https://github.com/comfyanonymous/ComfyUI/commit/6bd3f8eb9ff2d7c74e8ca75ad1f854a6b256b714 __auto-added__
- 2025-10-06T18:49:04+00:00: v0.3.63 - https://github.com/comfyanonymous/ComfyUI/releases/tag/v0.3.63 __auto-added__
- 2025-10-06T20:31:14+00:00: ComfyUI 0.3.63: Subgraph Publishing, Selection Toolbox Redesign - https://blog.comfy.org/p/comfyui-0363-subgraph-publishing __auto-added__
- 2025-10-06T23:05:57+00:00: fix(api-nodes): enable more pylint rules (#10213) - https://github.com/comfyanonymous/ComfyUI/commit/6ae35158013e50698e680344ab1f54de0d59fef0 __auto-added__
- 2025-10-06T23:20:26+00:00: convert nodes_pika.py to V3 schema (#10216) - https://github.com/comfyanonymous/ComfyUI/commit/e77e0a8f8fdcdc53deb8207e0d5b16ca56824a4b __auto-added__
- 2025-10-06T23:26:52+00:00: convert nodes_kling.py to V3 schema (#10236) - https://github.com/comfyanonymous/ComfyUI/commit/8c1991042795d06c7ccfd5d1931eb994044c75ef __auto-added__
- 2025-10-07T02:08:08+00:00: Implement gemma 3 as a text encoder. (#10241) - https://github.com/comfyanonymous/ComfyUI/commit/8aea746212dc1bb1601b4dc5e8c8093d2221d89c __auto-added__
- 2025-10-07T03:08:12+00:00: v0.5.0 - https://github.com/Comfy-Org/desktop/releases/tag/v0.5.0 __auto-added__
- 2025-10-07T20:15:32+00:00: fix(ReCraft-API-node): allow custom multipart parser to return FormDa… - https://github.com/comfyanonymous/ComfyUI/commit/fc34c3d1125e970699dcb311323839ed6dda4985 __auto-added__
- 2025-10-07T21:11:37+00:00: feat(api-nodes): add Sora2 API node (#10249) - https://github.com/comfyanonymous/ComfyUI/commit/9e984c48bc6a1d1c82231c46542995dbf5a265d7 __auto-added__
- 2025-10-07T23:55:23+00:00: Temp fix for LTXV custom nodes. (#10251) - https://github.com/comfyanonymous/ComfyUI/commit/8a15568f10c0622a7281c32fadffc51511e53c10 __auto-added__
- 2025-10-08T00:44:50+00:00: v1.27.10 - https://github.com/Comfy-Org/ComfyUI_frontend/releases/tag/v1.27.10 __auto-added__
- 2025-10-08T00:54:00+00:00: Bump frontend to 1.27.10 (#10252) - https://github.com/comfyanonymous/ComfyUI/commit/19f595b788bd227004a5f7232f3b5895b46411ea __auto-added__
- 2025-10-08T01:13:49+00:00: Sora 2 API Nodes Now in ComfyUI - https://blog.comfy.org/p/sora-2-api-nodes-now-in-comfyui __auto-added__
- 2025-10-08T02:48:51+00:00: update template to 0.1.94 (#10253) - https://github.com/comfyanonymous/ComfyUI/commit/51697d50dc94005b1c279eb0cf45207697946020 __auto-added__
- 2025-10-08T04:53:43+00:00: ComfyUI version 0.3.64 - https://github.com/comfyanonymous/ComfyUI/commit/637221995f7424a561bd825de3e61ea117dfe1e3 __auto-added__
- 2025-10-08T04:53:43+00:00: v0.3.64 - https://github.com/comfyanonymous/ComfyUI/releases/tag/v0.3.64 __auto-added__
- 2025-10-08T05:24:46+00:00: v0.5.1 - https://github.com/Comfy-Org/desktop/releases/tag/v0.5.1 __auto-added__
- 2025-10-08T07:14:04+00:00: feat(V3-io): allow Enum classes for Combo options (#10237) - https://github.com/comfyanonymous/ComfyUI/commit/3e0eb8d33f9a65f2a01430f1b4a1535348af881c __auto-added__
- 2025-10-08T15:27:50+00:00: 5.5.0 - https://github.com/runpod-workers/worker-comfyui/releases/tag/5.5.0 __auto-added__
- 2025-10-08T19:52:23+00:00: v1.29.0 - https://github.com/Comfy-Org/ComfyUI_frontend/releases/tag/v1.29.0 __auto-added__
- 2025-10-08T21:49:02+00:00: Refactor model sampling sigmas code. (#10250) - https://github.com/comfyanonymous/ComfyUI/commit/6e59934089df3375e39db174340b6a937b226c83 __auto-added__
- 2025-10-09T00:30:41+00:00: Mvly/node update (#10042) - https://github.com/comfyanonymous/ComfyUI/commit/72c2071972d3207ed92bc20535299c5f39622818 __auto-added__
- 2025-10-09T06:14:00+00:00: convert nodes_latent.py to V3 schema (#10160) - https://github.com/comfyanonymous/ComfyUI/commit/cbee7d33909f168a08ab7e53d897ea284a304d84 __auto-added__
- 2025-10-09T20:37:35+00:00: More surgical fix for #10267 (#10276) - https://github.com/comfyanonymous/ComfyUI/commit/139addd53c6cab97fb0ac28d1c895b3ecc7dff6c __auto-added__
- 2025-10-09T22:18:23+00:00: convert nodes_sd3.py and nodes_slg.py to V3 schema (#10162) - https://github.com/comfyanonymous/ComfyUI/commit/fc0fbf141c7deb444fe730af2f2db8e2beddaf60 __auto-added__
- 2025-10-09T23:08:40+00:00: convert nodes_upscale_model.py to V3 schema (#10149) - https://github.com/comfyanonymous/ComfyUI/commit/81e4dac107c24b1655babc47c99c33551c96a644 __auto-added__
- 2025-10-10T21:33:51+00:00: Fix save audio nodes saving mono audio as stereo. (#10289) - https://github.com/comfyanonymous/ComfyUI/commit/cdfc25a1605add750a3b1a83360b84e8e95324c6 __auto-added__
- 2025-10-10T23:21:40+00:00: feat(api-nodes): add price extractor feature; small fixes to Kling & … - https://github.com/comfyanonymous/ComfyUI/commit/14d642acd66973c81a806dc6f0562d89b4ba3506 __auto-added__
- 2025-10-11T03:32:00+00:00: v1.29.1 - https://github.com/Comfy-Org/ComfyUI_frontend/releases/tag/v1.29.1 __auto-added__
- 2025-10-11T17:27:22+00:00: Update template to 0.1.95 (#10294) - https://github.com/comfyanonymous/ComfyUI/commit/f43b8ab2a2eda034651187222829f72aa82eae6c __auto-added__
- 2025-10-12T02:57:23+00:00: Implement the mmaudio VAE. (#10300) - https://github.com/comfyanonymous/ComfyUI/commit/84e9ce32c6d9d340404ee0798a426dae52bbee8b __auto-added__
- 🔥 2025-10-12T04:28:01+00:00: Improve AMD performance. (#10302) - https://github.com/comfyanonymous/ComfyUI/commit/a125cd84b054a57729b5eecab930ca9408719832 __priority-auto-added__
- 2025-10-13T03:32:02+00:00: Update node docs to 0.3.0 (#10318) - https://github.com/comfyanonymous/ComfyUI/commit/fdc92863b6dc6d0edff85e6dbb6a2382046c020d __auto-added__
- 2025-10-13T03:54:41+00:00: Update the extra_model_paths.yaml.example (#10319) - https://github.com/comfyanonymous/ComfyUI/commit/d68ece7301c63da11e0b565da0ecc2900c8ea447 __auto-added__
- 2025-10-13T18:57:27+00:00: Always set diffusion model to eval() mode. (#10331) - https://github.com/comfyanonymous/ComfyUI/commit/e693e4db6a2df8482599eed348be15f87799b910 __auto-added__
- 2025-10-13T19:14:52+00:00: add indent=4 kwarg to json.dumps() (#10307) - https://github.com/comfyanonymous/ComfyUI/commit/27ffd12c45d4237338fe8789779313db9bab59f1 __auto-added__
- 2025-10-13T19:23:11+00:00: WAN2.2: Fix cache VRAM leak on error (#10308) - https://github.com/comfyanonymous/ComfyUI/commit/95ca2e56c82c1c714dba685bd81ebf3f7baf8efa __auto-added__
- 2025-10-13T19:36:26+00:00: convert nodes_hunyuan.py to V3 schema (#10136) - https://github.com/comfyanonymous/ComfyUI/commit/3dfdcf66b643b6c191743d3b30fd8198ce690f2d __auto-added__
- 2025-10-13T23:56:15+00:00: ComfyUI on NVIDIA DGX Spark - https://blog.comfy.org/p/comfyui-on-nvidia-dgx-spark __auto-added__
- 2025-10-14T02:18:58+00:00: Fix loading old stable diffusion ckpt files on newer numpy. (#10333) - https://github.com/comfyanonymous/ComfyUI/commit/e4ea3936660a8f8dfa2467e51631362b04ad47e8 __auto-added__
- 2025-10-14T02:37:19+00:00: Better memory estimation for the SD/Flux VAE on AMD. (#10334) - https://github.com/comfyanonymous/ComfyUI/commit/dfff7e5332530b7278c1f90c51aed525db53489e __auto-added__
- 2025-10-14T03:10:30+00:00: 🚀 ComfyUI Frontend v1.29.2 - https://github.com/Comfy-Org/ComfyUI_frontend/releases/tag/v1.29.2 __auto-added__
- 2025-10-14T03:39:55+00:00: ComfyUI version 0.3.65 - https://github.com/comfyanonymous/ComfyUI/commit/51696e3fdcdfad657cb15854345fbcbbe70eef8d __auto-added__
- 2025-10-14T03:39:55+00:00: v0.3.65 - https://github.com/comfyanonymous/ComfyUI/releases/tag/v0.3.65 __auto-added__
- 2025-10-14T03:43:53+00:00: Faster workflow cancelling. (#10301) - https://github.com/comfyanonymous/ComfyUI/commit/3374e900d0f310100ebe54944175a36f287110cb __auto-added__
- 2025-10-14T05:09:19+00:00: v0.5.2 - https://github.com/Comfy-Org/desktop/releases/tag/v0.5.2 __auto-added__
- 2025-10-14T06:09:12+00:00: Python 3.14 instructions. (#10337) - https://github.com/comfyanonymous/ComfyUI/commit/84867067ea588e2a3d38a54dc34d86c96d706487 __auto-added__
- 2025-10-14T06:55:56+00:00: api-nodes: fixed dynamic pricing format; import comfy_io directly (#1… - https://github.com/comfyanonymous/ComfyUI/commit/7a883849ea21003a5a649276a4cd322cb6c2ff0b __auto-added__
- 2025-10-15T01:08:23+00:00: Bump frontend to 1.28.6 (#10345) - https://github.com/comfyanonymous/ComfyUI/commit/ddfce1af4fc76768dbdd0cc4fa22d47b20a8b876 __auto-added__
- 2025-10-15T04:21:11+00:00: gfx942 doesn't support fp8 operations. (#10348) - https://github.com/comfyanonymous/ComfyUI/commit/1c10b33f9bbc75114053bc041851b60767791783 __auto-added__
- 2025-10-15T22:12:25+00:00: Add TemporalScoreRescaling node (#10351) - https://github.com/comfyanonymous/ComfyUI/commit/f72c6616b2e91e4021591895192cef8b9d4d1c75 __auto-added__
- 2025-10-15T22:41:45+00:00: feat(api-nodes): add Veo3.1 model (#10357) - https://github.com/comfyanonymous/ComfyUI/commit/74b7f0b04ba19926286518b0a0179290b79bfae0 __auto-added__
- 🔥 2025-10-15T22:48:12+00:00: Latest pytorch stable is cu130 (#10361) - https://github.com/comfyanonymous/ComfyUI/commit/6b035bfce25b5336ed2a39c72972a8a36a80f9bd __priority-auto-added__
- 2025-10-15T23:47:26+00:00: Fix order of inputs nested merge_nested_dicts (#10362) - https://github.com/comfyanonymous/ComfyUI/commit/493b81e48f4067da95e4cee36d42a3516338da79 __auto-added__
- 2025-10-16T00:16:09+00:00: refactor: Replace manual patches merging with merge_nested_dicts (#10… - https://github.com/comfyanonymous/ComfyUI/commit/afa8a24fe1f81d447b961fdf41f47f9094d28919 __auto-added__
- 2025-10-16T03:16:28+00:00: v1.28.7 - https://github.com/Comfy-Org/ComfyUI_frontend/releases/tag/v1.28.7 __auto-added__
- 2025-10-16T03:30:39+00:00: Bump frontend to 1.28.7 (#10364) - https://github.com/comfyanonymous/ComfyUI/commit/55ac7d333c55d808be33c590a4a2e6c965d5f9a8 __auto-added__
- 2025-10-16T03:25:25+00:00: Veo 3.1 is now available in ComfyUI! - https://blog.comfy.org/p/veo-31-is-now-available-in-comfyui __auto-added__
- 2025-10-16T08:13:31+00:00: feat: deprecated API alert (#10366) - https://github.com/comfyanonymous/ComfyUI/commit/4054b4bf38d11fc0c784c2d19f5fc0ed3bbc7ae4 __auto-added__
- 2025-10-16T17:12:50+00:00: fix(api-nodes): remove "veo2" model from Veo3 node (#10372) - https://github.com/comfyanonymous/ComfyUI/commit/bc0ad9bb49b642e081f99f92d239d634988d52bc __auto-added__
- 🔥 2025-10-16T22:16:03+00:00: Workaround for nvidia issue where VAE uses 3x more memory on torch 2.… - https://github.com/comfyanonymous/ComfyUI/commit/19b466160c1cd43f707769adef6f8ed6e9fd50bf __priority-auto-added__
- 2025-10-16T23:59:56+00:00: workaround also works on cudnn 91200 (#10375) - https://github.com/comfyanonymous/ComfyUI/commit/b1293d50eff5f1ff2e54f73114fbe7c0f9aef8fe __auto-added__
- 2025-10-17T02:15:55+00:00: 🚀 ComfyUI Frontend v1.30.0 - https://github.com/Comfy-Org/ComfyUI_frontend/releases/tag/v1.30.0 __auto-added__
- 2025-10-17T02:34:47+00:00: Introducing ImagenWorld: A Real World Benchmark for Image Generation and Editing - https://blog.comfy.org/p/introducing-imagenworld __auto-added__
- 2025-10-17T04:39:37+00:00: Do batch_slice in EasyCache's apply_cache_diff (#10376) - https://github.com/comfyanonymous/ComfyUI/commit/d8d60b56093a15edc5d25486d387d3c5917dc3d3 __auto-added__
- 2025-10-17T20:55:15+00:00: execution: fold in dependency aware caching / Fix --cache-none with l… - https://github.com/comfyanonymous/ComfyUI/commit/b1467da4803017a418c32c159525767f45871ca3 __auto-added__
- 2025-10-17T21:13:05+00:00: convert nodes_controlnet.py to V3 schema (#10202) - https://github.com/comfyanonymous/ComfyUI/commit/99ce2a1f66c4bcd500d76cc9a7430f7b2bf32776 __auto-added__
- 2025-10-17T22:22:59+00:00: Update Python 3.14 installation instructions (#10385) - https://github.com/comfyanonymous/ComfyUI/commit/92d97380bd02d9883295aeb2d29365cecd9a765e __auto-added__
- 🔥 2025-10-18T00:03:28+00:00: Disable torch compiler for cast_bias_weight function (#10384) - https://github.com/comfyanonymous/ComfyUI/commit/9da397ea2f271080406f0c14cf4f0db7221ddf70 __priority-auto-added__
- 2025-10-18T11:26:13+00:00: v1.30.1 - https://github.com/Comfy-Org/ComfyUI_frontend/releases/tag/v1.30.1 __auto-added__
- 🔥 2025-10-19T02:35:46+00:00: Turn off cuda malloc by default when --fast autotune is turned on. (#… - https://github.com/comfyanonymous/ComfyUI/commit/5b80addafd24bda5b2f9f7a35e32dbd40823c3fd __priority-auto-added__
- 2025-10-19T03:19:52+00:00: Speed up chroma radiance. (#10395) - https://github.com/comfyanonymous/ComfyUI/commit/dad076aee68ab676fb390d9663ab9e343824a080 __auto-added__
- 🔥 2025-10-19T05:25:35+00:00: Pytorch is stupid. (#10398) - https://github.com/comfyanonymous/ComfyUI/commit/b4f30bd4087a79b4c4fc89bb67b9889adb866294 __priority-auto-added__
- 2025-10-19T20:05:46+00:00: Deprecation warning on unused files (#10387) - https://github.com/comfyanonymous/ComfyUI/commit/b5c59b763c6b14e1362ec4274b09eca4f3f7091b __auto-added__
- 2025-10-20T19:28:36+00:00: Update template to 0.2.1 (#10413) - https://github.com/comfyanonymous/ComfyUI/commit/a4787ac83bf6c83eeb459ed80fc9b36f63d2a3a7 __auto-added__
- 2025-10-20T19:43:24+00:00: Log message for cudnn disable on  AMD. (#10418) - https://github.com/comfyanonymous/ComfyUI/commit/2c2aa409b01f513de88d2245931e5836ed1cd718 __auto-added__
- 2025-10-20T23:03:06+00:00: Revert "execution: fold in dependency aware caching / Fix --cache-non… - https://github.com/comfyanonymous/ComfyUI/commit/b7992f871af38d89a459080caa57cc359ed93a46 __auto-added__
- 2025-10-21T05:12:32+00:00: ComfyUI version v0.3.66 - https://github.com/comfyanonymous/ComfyUI/commit/560b1bdfca77d9441ca2924fd9d6baa8dda05cd7 __auto-added__
- 2025-10-21T05:12:32+00:00: v0.3.66 - https://github.com/comfyanonymous/ComfyUI/releases/tag/v0.3.66 __auto-added__
- 2025-10-21T19:28:01+00:00: v0.5.3 - https://github.com/Comfy-Org/desktop/releases/tag/v0.5.3 __auto-added__
- 2025-10-21T20:05:40+00:00: New in ComfyUI: Easy Subgraph Editing & New Template Library - https://blog.comfy.org/p/comfyui-0366-updates __auto-added__
- 2025-10-21T21:16:02+00:00: v1.29.3 - https://github.com/Comfy-Org/ComfyUI_frontend/releases/tag/v1.29.3 __auto-added__
- 2025-10-21T23:15:23+00:00: Only disable cudnn on newer AMD GPUs. (#10437) - https://github.com/comfyanonymous/ComfyUI/commit/9cdc64998f8990aed7688b0ebe89bc3b97733764 __auto-added__
- 2025-10-22T03:16:16+00:00: Add custom node published subgraphs endpoint (#10438) - https://github.com/comfyanonymous/ComfyUI/commit/f13cff0be65e35d34876b173bba2fec6bd94746b __auto-added__
- 2025-10-22T19:49:05+00:00: execution: fold in dependency aware caching / Fix --cache-none with l… - https://github.com/comfyanonymous/ComfyUI/commit/4739d7717fea56750d0ef98c64268d9c1e487d78 __auto-added__
- 2025-10-22T21:26:22+00:00: Small readme improvement. (#10442) - https://github.com/comfyanonymous/ComfyUI/commit/a1864c01f29cc43fe6bf823fc3fd46ba2781c2e0 __auto-added__
- 2025-10-22T22:44:50+00:00: v1.30.2 - https://github.com/Comfy-Org/ComfyUI_frontend/releases/tag/v1.30.2 __auto-added__
- 2025-10-24T01:21:14+00:00: WIP way to support multi multi dimensional latents. (#10456) - https://github.com/comfyanonymous/ComfyUI/commit/1bcda6df987a6c92b39d8b6d29e0b029450d67d0 __auto-added__
- 2025-10-24T05:37:16+00:00: feat(api-nodes): network client v2: async ops, cancellation, download… - https://github.com/comfyanonymous/ComfyUI/commit/388b306a2b48070737b092b51e76de933baee9ad __auto-added__
- 2025-10-24T22:48:34+00:00: convert Tripo API nodes to V3 schema (#10469) - https://github.com/comfyanonymous/ComfyUI/commit/dd5af0c5871376c377b2e30f9725b67a768eea6f __auto-added__
- 2025-10-24T23:56:51+00:00: Remove useless function (#10472) - https://github.com/comfyanonymous/ComfyUI/commit/426cde37f10dc391f9601ab938e02c0faa42db14 __auto-added__
- 2025-10-25T02:24:56+00:00: v1.30.3 - https://github.com/Comfy-Org/ComfyUI_frontend/releases/tag/v1.30.3 __auto-added__
- 2025-10-25T21:35:30+00:00: convert Gemini API nodes to V3 schema (#10476) - https://github.com/comfyanonymous/ComfyUI/commit/e86b79ab9ea7e740b80490353f3f5763840ede81 __auto-added__
- 🔥 2025-10-26T00:05:22+00:00: Add warning for torch-directml usage (#10482) - https://github.com/comfyanonymous/ComfyUI/commit/098a352f136c610071bcb74f13e5b0ca16e6e7b3 __priority-auto-added__
- 2025-10-26T03:07:29+00:00: Fix mistake. (#10484) - https://github.com/comfyanonymous/ComfyUI/commit/f6bbc1ac846b7d9a73ae50c3a45cf5a41058c54d __auto-added__
- 2025-10-26T06:51:06+00:00: fix(api-nodes): random issues on Windows by capturing general OSError… - https://github.com/comfyanonymous/ComfyUI/commit/9d529e53084bdec28f684f3886a26c93598e7338 __auto-added__
- 🔥 2025-10-27T00:23:01+00:00: Bump portable deps workflow to torch cu130 python 3.13.9 (#10493) - https://github.com/comfyanonymous/ComfyUI/commit/c170fd2db598a0bdce56f80e22e83e10ad731421 __priority-auto-added__
- 2025-10-27T00:22:46+00:00: v1.31.0 - https://github.com/Comfy-Org/ComfyUI_frontend/releases/tag/v1.31.0 __auto-added__
- 2025-10-28T03:54:00+00:00: Add a bat to run comfyui portable without api nodes. (#10504) - https://github.com/comfyanonymous/ComfyUI/commit/601ee1775a3c06c9b4de1fa7d808af8625b2fcd5 __auto-added__
- 2025-10-28T05:25:29+00:00: feat(api-nodes): add LTXV API nodes (#10496) - https://github.com/comfyanonymous/ComfyUI/commit/55bad303754eb60fa98f3ccf598e95502b819149 __auto-added__
- 2025-10-28T05:56:30+00:00: Update template to 0.2.4 (#10505) - https://github.com/comfyanonymous/ComfyUI/commit/6abc30aae9bd13f31dafd32552a365f2df2cf715 __auto-added__
- 2025-10-28T07:03:59+00:00: ComfyUI version v0.3.67 - https://github.com/comfyanonymous/ComfyUI/commit/f2bb3230b796f6a486894fc3b597db2c0b9538c9 __auto-added__
- 2025-10-28T07:03:59+00:00: v0.3.67 - https://github.com/comfyanonymous/ComfyUI/releases/tag/v0.3.67 __auto-added__
- 2025-10-28T07:23:52+00:00: Remove comfy api key from queue api. (#10502) - https://github.com/comfyanonymous/ComfyUI/commit/8cf2ba4ba64203551276513068ee81145e90f0bc __auto-added__
- 2025-10-28T08:45:45+00:00: Tell users to update nvidia drivers if problem with portable. (#10510) - https://github.com/comfyanonymous/ComfyUI/commit/3bea4efc6b23d76c6b0672cd90421a9024e13fdb __auto-added__
- 2025-10-28T18:49:07+00:00: v1.28.8 - https://github.com/Comfy-Org/ComfyUI_frontend/releases/tag/v1.28.8 __auto-added__
- 2025-10-28T19:08:08+00:00: Tell users to update their nvidia drivers if portable doesn't start. … - https://github.com/comfyanonymous/ComfyUI/commit/22e40d2ace0f53da025b3a41cbe4b664ef807097 __auto-added__
- 2025-10-28T20:22:08+00:00: execution: Allow a subgraph nodes to execute multiple times (#10499) - https://github.com/comfyanonymous/ComfyUI/commit/d202c2ba7404affd58a2199aeb514b3cc48e0ef3 __auto-added__
- 2025-10-28T21:38:05+00:00: convert nodes_recraft.py to V3 schema (#10507) - https://github.com/comfyanonymous/ComfyUI/commit/210f7a1ba580d57d817ca68346cb72b8d0a26ad2 __auto-added__
- 2025-10-28T22:07:45+00:00: v1.31.1 - https://github.com/Comfy-Org/ComfyUI_frontend/releases/tag/v1.31.1 __auto-added__
- 2025-10-28T21:54:31+00:00: LTX-2 Now Available in ComfyUI! - https://blog.comfy.org/p/ltx-2-now-available-in-comfyui __auto-added__
- 2025-10-28T22:16:54+00:00: v0.5.4 - https://github.com/Comfy-Org/desktop/releases/tag/v0.5.4 __auto-added__
- 2025-10-29T04:37:00+00:00: Fix issue. (#10527) - https://github.com/comfyanonymous/ComfyUI/commit/e525673f7201b6c49af0fa0e6baf44e4e98bb10c __auto-added__
- 2025-10-29T16:25:18+00:00: Comfy Challenge #8: Spooky Renders! - https://blog.comfy.org/p/comfy-challenge-8-spooky-renders __auto-added__
- 2025-10-29T18:14:56+00:00: use new API client in Luma and Minimax nodes (#10528) - https://github.com/comfyanonymous/ComfyUI/commit/6c14f3afac0ea28dba24fe8783e7c1f09c03b31f __auto-added__
- 2025-10-29T19:43:51+00:00: Reduce memory usage for fp8 scaled op. (#10531) - https://github.com/comfyanonymous/ComfyUI/commit/1a58087ac2eb64be3645934d0025aafaa5bdce38 __auto-added__
- 2025-10-29T19:48:06+00:00: Fix case of weights not being unpinned. (#10533) - https://github.com/comfyanonymous/ComfyUI/commit/ec4fc2a09a390d0d81500c51fb9e4d8a7a5ce1fc __auto-added__
- 2025-10-29T21:20:27+00:00: Try to fix slow load issue on low ram hardware with pinned mem. (#10536) - https://github.com/comfyanonymous/ComfyUI/commit/25de7b1bfa22dd98922f047a1342cc97f8e46c5b __auto-added__
- 2025-10-29T23:37:06+00:00: Add units/info for the numbers displayed on 'load completely' and 'lo… - https://github.com/comfyanonymous/ComfyUI/commit/998bf60bebd03e57a55e106434657849342b733f __auto-added__
- 2025-10-30T06:49:03+00:00: use new API client in Pixverse and Ideogram nodes (#10543) - https://github.com/comfyanonymous/ComfyUI/commit/163b629c70a349c7d1e91eebc5365713e770af8a __auto-added__
- 2025-10-30T17:06:53+00:00: v0.5.5 - https://github.com/Comfy-Org/desktop/releases/tag/v0.5.5 __auto-added__
- 2025-10-30T17:22:35+00:00: fix img2img operation in Dall2 node (#10552) - https://github.com/comfyanonymous/ComfyUI/commit/dfac94695be95076d8028d04005a744f3ec0de8d __auto-added__
- 2025-10-30T21:39:02+00:00: Add RAM Pressure cache mode (#10454) - https://github.com/comfyanonymous/ComfyUI/commit/513b0c46fba3bf40191d684ff81207ad935f1717 __auto-added__
- 2025-10-31T02:11:38+00:00: Add a ScaleROPE node. Currently only works on WAN models. (#10559) - https://github.com/comfyanonymous/ComfyUI/commit/614cf9805e1056216487a2d1b1a07206d77f87e7 __auto-added__
- 2025-10-31T02:51:58+00:00: Fix rope scaling. (#10560) - https://github.com/comfyanonymous/ComfyUI/commit/27d1bd882925e3bbdffb405cea098ac52bb20ac5 __auto-added__
- 2025-10-31T04:14:52+00:00: v1.32.0 - https://github.com/Comfy-Org/ComfyUI_frontend/releases/tag/v1.32.0 __auto-added__
- 2025-10-31T19:41:40+00:00: ScaleROPE now works on Lumina models. (#10578) - https://github.com/comfyanonymous/ComfyUI/commit/7f374e42c833c69c71605507b90f79cc26d14a71 __auto-added__
- 🔥 2025-11-01T04:25:17+00:00: Fix torch compile regression on fp8 ops. (#10580) - https://github.com/comfyanonymous/ComfyUI/commit/c58c13b2bad6df0de93cc0cf107e96522a3cb5b3 __priority-auto-added__
- 2025-11-01T19:14:06+00:00: convert StabilityAI to use new API client (#10582) - https://github.com/comfyanonymous/ComfyUI/commit/20182a393f43ab1fdf798f8da6aac0ef6116e7e6 __auto-added__
- 2025-11-01T21:25:59+00:00: Fix issue with pinned memory. (#10597) - https://github.com/comfyanonymous/ComfyUI/commit/44869ff786dc90b36172fd766c9a110e4c40c04b __auto-added__
- 2025-11-01T22:48:53+00:00: Small speed improvements to --async-offload (#10593) - https://github.com/comfyanonymous/ComfyUI/commit/135fa49ec23320834f774cf3def9e51ad3773f86 __auto-added__
- 2025-11-02T18:14:04+00:00: Clarify help text for --fast argument (#10609) - https://github.com/comfyanonymous/ComfyUI/commit/97ff9fae7e728cffdfc3aee6d72aa1e0d0b78702 __auto-added__
- 2025-11-02T21:44:40+00:00: v1.32.1 - https://github.com/Comfy-Org/ComfyUI_frontend/releases/tag/v1.32.1 __auto-added__
- 2025-11-03T08:16:40+00:00: fix(caching): treat bytes as hashable (#10567) - https://github.com/comfyanonymous/ComfyUI/commit/88df172790b8ed7b2e6ea7c0f0bd63ca3553921b __auto-added__
- 2025-11-03T08:29:08+00:00: feat(Pika-API-nodes): use new API client (#10608) - https://github.com/comfyanonymous/ComfyUI/commit/4e2110c794b187c9326d604e7c0b0a4fad81148a __auto-added__
- 2025-11-03T18:59:44+00:00: chore: update embedded docs to v0.3.1 (#10614) - https://github.com/comfyanonymous/ComfyUI/commit/e974e554ca23be505b72bc9c1614f4285c1db6e3 __auto-added__
- 🔥 2025-11-03T22:08:30+00:00: People should update their pytorch versions. (#10618) - https://github.com/comfyanonymous/ComfyUI/commit/958a17199ac519504e390ea0d53295ceb8cbd2c1 __priority-auto-added__
- 🔥 2025-11-03T22:37:12+00:00: Speed up torch.compile (#10620) - https://github.com/comfyanonymous/ComfyUI/commit/0652cb8e2d343f68e38285755835c77bda7f6389 __priority-auto-added__
- 2025-11-03T22:58:24+00:00: Fixes (#10621) - https://github.com/comfyanonymous/ComfyUI/commit/e199c8cc6758d388792fd66b99e8de832814ff91 __auto-added__
- 🔥 2025-11-04T00:22:10+00:00: Bring back fp8 torch compile performance to what it should be. (#10622) - https://github.com/comfyanonymous/ComfyUI/commit/6b88478f9fe0874c0e17468c9fca3a0a84e6c781 __priority-auto-added__
- 🔥 2025-11-04T03:14:20+00:00: More fp8 torch.compile regressions fixed. (#10625) - https://github.com/comfyanonymous/ComfyUI/commit/af4b7b5edb339a15aa443e32aefbceac1810baa0 __priority-auto-added__
- 2025-11-04T16:34:22+00:00: Comfy Cloud is Now in Public Beta - https://blog.comfy.org/p/comfy-cloud-is-now-in-public-beta __auto-added__
- 2025-11-04T18:51:53+00:00: chore: update workflow templates to v0.2.11 (#10634) - https://github.com/comfyanonymous/ComfyUI/commit/9c71a667904a049975531f2a7dd55f4a8fc92652 __auto-added__
- 2025-11-04T22:14:10+00:00: caching: Handle None outputs tuple case (#10637) - https://github.com/comfyanonymous/ComfyUI/commit/a389ee01bb7ba5174729906a7f85bd08b5c2cb87 __auto-added__
- 2025-11-04T22:37:50+00:00: Limit amount of pinned memory on windows to prevent issues. (#10638) - https://github.com/comfyanonymous/ComfyUI/commit/7f3e4d486cd77c3ad30eb4714ec18bdaf29e2b5c __auto-added__
- 2025-11-05T00:42:23+00:00: ComfyUI version v0.3.68 - https://github.com/comfyanonymous/ComfyUI/commit/265adad858e1f31b66cd3523a02b16f5d34ced52 __auto-added__
- 2025-11-05T00:42:23+00:00: v0.3.68 - https://github.com/comfyanonymous/ComfyUI/releases/tag/v0.3.68 __auto-added__
- 2025-11-05T01:10:11+00:00: Use single apply_rope function across models (#10547) - https://github.com/comfyanonymous/ComfyUI/commit/4cd881866bad0cde70273cc123d725693c1f2759 __auto-added__
- 2025-11-05T03:47:35+00:00: Lower ltxv mem usage to what it was before previous pr. (#10643) - https://github.com/comfyanonymous/ComfyUI/commit/c4a6b389de1014471a75a46ee57d2fdac4f8df93 __auto-added__
- 2025-11-05T10:16:00+00:00: feat(API-nodes): move Rodin3D nodes to new client; removed old api cl… - https://github.com/comfyanonymous/ComfyUI/commit/bda0eb2448135797d5a72f7236ce26d07e555baf __auto-added__
- 2025-11-05T21:09:44+00:00: v1.32.2 - https://github.com/Comfy-Org/ComfyUI_frontend/releases/tag/v1.32.2 __auto-added__
- 2025-11-05T21:09:12+00:00: Comfy Challenge #9 : Cloudcrafted! - https://blog.comfy.org/p/comfy-challenge-9-cloudcrafted __auto-added__
- 2025-11-05T23:08:13+00:00: Enable pinned memory by default on Nvidia. (#10656) - https://github.com/comfyanonymous/ComfyUI/commit/1d69245981f9fb3861018613246042296d887dd3 __auto-added__
- 2025-11-06T00:11:15+00:00: Pinned mem also seems to work on AMD. (#10658) - https://github.com/comfyanonymous/ComfyUI/commit/09dc24c8a982776abd5cb2f71e3d041139e1d5b2 __auto-added__
- 2025-11-06T09:11:30+00:00: Clarify release cycle. (#10667) - https://github.com/comfyanonymous/ComfyUI/commit/e05c90712670fa4a2ffebd44046fc78747193a36 __auto-added__
- 2025-11-07T02:20:48+00:00: mm: guard against double pin and unpin explicitly (#10672) - https://github.com/comfyanonymous/ComfyUI/commit/cf97b033ee80cf245b4592d42f89e6de67e409a4 __auto-added__
- 2025-11-07T16:15:05+00:00: Only unpin tensor if it was pinned by ComfyUI (#10677) - https://github.com/comfyanonymous/ComfyUI/commit/a1a70362ca376cff05a0514e0ce771ab26d92fd9 __auto-added__
- 2025-11-08T04:52:25+00:00: v1.32.3 - https://github.com/Comfy-Org/ComfyUI_frontend/releases/tag/v1.32.3 __auto-added__
- 2025-11-08T19:25:54+00:00: v1.32.4 - https://github.com/Comfy-Org/ComfyUI_frontend/releases/tag/v1.32.4 __auto-added__
- 2025-11-08T20:52:02+00:00: Make ScaleROPE node work on Flux. (#10686) - https://github.com/comfyanonymous/ComfyUI/commit/2abd2b5c2049a9625b342bcb7decedd5d1645f66 __auto-added__
- 2025-11-09T23:06:39+00:00: Add logging for model unloading. (#10692) - https://github.com/comfyanonymous/ComfyUI/commit/e632e5de281b91dd7199636dd6d82126fbfb07d5 __auto-added__
- 2025-11-09T23:51:33+00:00: Unload weights if vram usage goes up between runs. (#10690) - https://github.com/comfyanonymous/ComfyUI/commit/dea899f22125d38a8b48147d6cce89a2b659fdeb __auto-added__
- 2025-11-10T03:52:11+00:00: ops: Put weight cast on the offload stream (#10697) - https://github.com/comfyanonymous/ComfyUI/commit/c350009236e5d172a3050c04043ea70a301378ca __auto-added__
- 2025-11-10T14:57:40+00:00: 5.5.1 - https://github.com/runpod-workers/worker-comfyui/releases/tag/5.5.1 __auto-added__
- 2025-11-10T20:35:29+00:00: Update CI workflow to remove dead macOS runner. (#10704) - https://github.com/comfyanonymous/ComfyUI/commit/5ebcab3c7d974963a89cecd37296a22fdb73bd2b __auto-added__
- 🔥 2025-11-12T00:33:30+00:00: Don't pin tensor if not a torch.nn.parameter.Parameter (#10718) - https://github.com/comfyanonymous/ComfyUI/commit/119941174704081a16a4c3f303d99f2fb1e95cde __priority-auto-added__
- 2025-11-12T20:21:05+00:00: Update README.md for Intel Arc GPU installation, remove IPEX (#10729) - https://github.com/comfyanonymous/ComfyUI/commit/e1d85e7577d8f6355bd4cb3449bcb0a7e5f80cb8 __auto-added__
- 2025-11-12T21:20:53+00:00: qwen: reduce VRAM usage (#10725) - https://github.com/comfyanonymous/ComfyUI/commit/1c7eaeca1013e4315f36e0d4d274faa106001121 __auto-added__
- 2025-11-12T22:04:41+00:00: Update Python 3.14 compatibility notes in README  (#10730) - https://github.com/comfyanonymous/ComfyUI/commit/8b0b93df51d04f08eb779cb84dc331fa18b43ae8 __auto-added__
- 2025-11-12T23:26:52+00:00: Quantized Ops fixes (#10715) - https://github.com/comfyanonymous/ComfyUI/commit/3b3ef9a77ac03ed516a45063f9736f33085cecca __auto-added__
- 2025-11-13T04:10:39+00:00: v1.32.5 - https://github.com/Comfy-Org/ComfyUI_frontend/releases/tag/v1.32.5 __auto-added__
- 2025-11-13T18:05:26+00:00: add PR template for API-Nodes (#10736) - https://github.com/comfyanonymous/ComfyUI/commit/f91078b1ffa484c424f78814f54de4d5846e4daa __auto-added__
- 2025-11-13T23:11:52+00:00: feat: add create_time dict to prompt field in /history and /queue (#1… - https://github.com/comfyanonymous/ComfyUI/commit/2fde9597f4b02c5f06c1a5ceb3ca2fa6d74966ec __auto-added__
- 2025-11-14T00:02:03+00:00: flux: reduce VRAM usage (#10737) - https://github.com/comfyanonymous/ComfyUI/commit/94c298f9625b0fd9af8ea07a73075fdefe0d9e57 __auto-added__
- 2025-11-14T02:32:39+00:00: Better instructions for the portable. (#10743) - https://github.com/comfyanonymous/ComfyUI/commit/1ef328c007a419c2c429df0f80532cc11579dc97 __auto-added__
- 2025-11-14T06:28:05+00:00: Use same code for chroma and flux blocks so that optimizations are sh… - https://github.com/comfyanonymous/ComfyUI/commit/f60923590c3f2fd05e166e2ec57968aaf7007dd0 __auto-added__
- 2025-11-14T08:26:05+00:00: Fix custom nodes import error. (#10747) - https://github.com/comfyanonymous/ComfyUI/commit/443056c401c53953bb8eee6da71b9ad29afe2581 __auto-added__
- 2025-11-15T11:54:40+00:00: Add left padding support to tokenizers. (#10753) - https://github.com/comfyanonymous/ComfyUI/commit/bd01d9f7fd241a45bd08b60dfedbe78577383cc4 __auto-added__
- 2025-11-15T19:18:49+00:00: chore(api-nodes): mark OpenAIDalle2 and OpenAIDalle3 nodes as depreca… - https://github.com/comfyanonymous/ComfyUI/commit/9a0238256873711bd38ce0e0b1d15a617a1ee454 __auto-added__
- 2025-11-15T20:37:34+00:00: Revert "chore(api-nodes): mark OpenAIDalle2 and OpenAIDalle3 nodes as… - https://github.com/comfyanonymous/ComfyUI/commit/2d4a08b717c492fa45e98bd70beb48d4e77cb464 __auto-added__
- 2025-11-16T08:01:14+00:00: Change ROCm nightly install command to 7.1 (#10764) - https://github.com/comfyanonymous/ComfyUI/commit/7d6103325e1c97aa54f963253e3e7f1d6da6947f __auto-added__
- 2025-11-17T22:17:24+00:00: ComfyUI version 0.3.69 - https://github.com/comfyanonymous/ComfyUI/commit/3d0003c24c1aec9f0c021dbc70ffb7cd8cf0685c __auto-added__
- 2025-11-17T22:17:24+00:00: v0.3.69 - https://github.com/comfyanonymous/ComfyUI/releases/tag/v0.3.69 __auto-added__
- 2025-11-18T00:04:04+00:00: Add release workflow for NVIDIA cu126 (#10777) - https://github.com/comfyanonymous/ComfyUI/commit/27cbac865ec226cfd9c1563327b0d62cf5dbd484 __auto-added__
- 2025-11-18T00:59:19+00:00: Update README with new portable download link (#10778) - https://github.com/comfyanonymous/ComfyUI/commit/f41e5f398d5d4059a3c87cf157bd932afcce3c0d __auto-added__
- 🔥 2025-11-18T03:04:06+00:00: Fix the portable download link for CUDA 12.6 (#10780) - https://github.com/comfyanonymous/ComfyUI/commit/fdf49a28617f742d746ad209e57ed7420b3535dc __priority-auto-added__
- 2025-11-18T05:26:44+00:00: Native block swap custom nodes considered harmful. (#10783) - https://github.com/comfyanonymous/ComfyUI/commit/47bfd5a33fa984a1102fc2bd7b25c91a69ace288 __auto-added__
- 2025-11-18T11:59:27+00:00: chore(api-nodes): adjusted PR template; set min python version for py… - https://github.com/comfyanonymous/ComfyUI/commit/048f49adbd19ac2d9c7c87682c832b7827a4b29d __auto-added__
- 2025-11-18T15:00:21+00:00: EasyCache: Fix for mismatch in input/output channels with some models… - https://github.com/comfyanonymous/ComfyUI/commit/e1ab6bb394b82fa654d5bc84043f97479d12f84c __auto-added__
- 2025-11-18T21:46:19+00:00: Fix hunyuan 3d 2.0 (#10792) - https://github.com/comfyanonymous/ComfyUI/commit/d52697457608a045cafc3b6d6cb89f0a49ba0709 __auto-added__
- 2025-11-18T20:40:01+00:00: v1.30.4 - https://github.com/Comfy-Org/ComfyUI_frontend/releases/tag/v1.30.4 __auto-added__
- 2025-11-18T22:26:44+00:00: feat(api-nodes): add new Gemini model (#10789) - https://github.com/comfyanonymous/ComfyUI/commit/24fdb92edf2e96fe757c480aa7f12be5bdfa3a15 __auto-added__
- 2025-11-19T00:37:20+00:00: ComfyUI 0.3.70 - https://github.com/comfyanonymous/ComfyUI/commit/b5c8be8b1db44ded07cb1b437b9f33ebff5848c1 __auto-added__
- 2025-11-19T00:37:20+00:00: v0.3.70 - https://github.com/comfyanonymous/ComfyUI/releases/tag/v0.3.70 __auto-added__
- 2025-11-19T03:36:03+00:00: Add a way to disable the final norm in the llama based TE models. (#1… - https://github.com/comfyanonymous/ComfyUI/commit/17027f2a6a20a31e2c6f3be2b1a06f39ad3a68d9 __auto-added__
- 2025-11-19T06:16:07+00:00: v1.32.6 - https://github.com/Comfy-Org/ComfyUI_frontend/releases/tag/v1.32.6 __auto-added__
- 2025-11-19T09:25:28+00:00: change display name of PreviewAny node to "Preview as Text" (#10796) - https://github.com/comfyanonymous/ComfyUI/commit/65ee24c9789b93660ebe978a3186486f105298c2 __auto-added__
- 2025-11-19T22:49:01+00:00: convert hunyuan3d.py to V3 schema (#10664) - https://github.com/comfyanonymous/ComfyUI/commit/6a1d3a1ae131f3fff7f45a7e835eb10e9d1338ee __auto-added__
- 2025-11-20T00:54:31+00:00: v1.33.1 - https://github.com/Comfy-Org/ComfyUI_frontend/releases/tag/v1.33.1 __auto-added__
- 2025-11-20T01:44:04+00:00: feat(api-nodes): add Topaz API nodes (#10755) - https://github.com/comfyanonymous/ComfyUI/commit/394348f5caaa062eac11a57e2997aacccd4246eb __auto-added__
- 2025-11-20T03:31:34+00:00: v1.33.2 - https://github.com/Comfy-Org/ComfyUI_frontend/releases/tag/v1.33.2 __auto-added__
- 2025-11-20T04:41:39+00:00: v0.5.6 - https://github.com/Comfy-Org/desktop/releases/tag/v0.5.6 __auto-added__
- 2025-11-20T04:56:23+00:00: Disable workaround on newer cudnn. (#10807) - https://github.com/comfyanonymous/ComfyUI/commit/cb96d4d18c78ee09d5fd70954ffcb4ad2c7f0d7a __auto-added__
- 2025-11-20T06:36:56+00:00: Update server templates handler to use new multi-package distribution… - https://github.com/comfyanonymous/ComfyUI/commit/87b0359392219841c2214e1eb06678840cae470e __auto-added__
- 2025-11-20T08:57:57+00:00: v1.33.3 - https://github.com/Comfy-Org/ComfyUI_frontend/releases/tag/v1.33.3 __auto-added__
- 2025-11-20T20:08:03+00:00: Fix ImageBatch with different channel count. (#10815) - https://github.com/comfyanonymous/ComfyUI/commit/f5e66d5e47271253edad5c4eddd817b0d6a23340 __auto-added__
- 2025-11-20T20:29:13+00:00: v0.5.7 - https://github.com/Comfy-Org/desktop/releases/tag/v0.5.7 __auto-added__
- 2025-11-20T22:42:46+00:00: Make Batch Images node add alpha channel when one of the inputs has i… - https://github.com/comfyanonymous/ComfyUI/commit/9e00ce5b76ec04be37375310512a443605b95077 __auto-added__
- 2025-11-21T00:33:54+00:00: fix(KlingLipSyncAudioToVideoNode): convert audio to mp3 format (#10811) - https://github.com/comfyanonymous/ComfyUI/commit/b75d349f25ccb702895c6f1b8af7aded63a7f7e2 __auto-added__
- 2025-11-21T00:21:36+00:00: v1.33.4 - https://github.com/Comfy-Org/ComfyUI_frontend/releases/tag/v1.33.4 __auto-added__
- 2025-11-21T02:20:52+00:00: bump comfyui-workflow-templates for nano banana 2 (#10818) - https://github.com/comfyanonymous/ComfyUI/commit/10e90a5757906ecdb71b84d41173813d7f62c140 __auto-added__
- 2025-11-21T03:44:43+00:00: HunyuanVideo 1.5 (#10819) - https://github.com/comfyanonymous/ComfyUI/commit/943b3b615d40542ea19bc8ff8ad2950c0a094605 __auto-added__
- 2025-11-21T04:08:08+00:00: v1.33.5 - https://github.com/Comfy-Org/ComfyUI_frontend/releases/tag/v1.33.5 __auto-added__
- 2025-11-21T04:39:37+00:00: Fix wrong path. (#10821) - https://github.com/comfyanonymous/ComfyUI/commit/33981237527a3d84d4e9c3b113f75d6dd37af6a4 __auto-added__
- 2025-11-21T05:49:13+00:00: ComfyUI 0.3.71 - https://github.com/comfyanonymous/ComfyUI/commit/c55fd7481626d8bee8044ea7512ea996d13a1b90 __auto-added__
- 2025-11-21T05:49:13+00:00: v0.3.71 - https://github.com/comfyanonymous/ComfyUI/releases/tag/v0.3.71 __auto-added__
- 2025-11-21T07:23:08+00:00: Meet Nano Banana Pro in ComfyUI! - https://blog.comfy.org/p/meet-nano-banana-pro-in-comfyui __auto-added__
- 2025-11-21T21:34:47+00:00: update frontend to 1.30 (#10793) - https://github.com/comfyanonymous/ComfyUI/commit/ecb683b057a19f1a05d18d6d0b0ee9a6c6c8f4a0 __auto-added__
- 2025-11-21T22:51:55+00:00: --disable-api-nodes now sets CSP header to force frontend offline. (#… - https://github.com/comfyanonymous/ComfyUI/commit/532938b16b544e4492ba0ffbe18b201b1a7bc55f __auto-added__
- 2025-11-22T10:28:29+00:00: Update requirements.txt (#10834) - https://github.com/comfyanonymous/ComfyUI/commit/a9c35256bccd4018fbe74bf1e857cc18bd1900ed __auto-added__
- 2025-11-22T23:37:08+00:00: v0.5.8 - https://github.com/Comfy-Org/desktop/releases/tag/v0.5.8 __auto-added__
- 2025-11-23T03:51:53+00:00: Add display names to Hunyuan latent video nodes. (#10837) - https://github.com/comfyanonymous/ComfyUI/commit/d89c29f25992713ec3102017c189858a457f1215 __auto-added__
- 2025-11-23T09:55:22+00:00: Add better error message for common error. (#10846) - https://github.com/comfyanonymous/ComfyUI/commit/cbd68e3d587a1b345bdc6ebcd8a8c6ba1a9d3af3 __auto-added__
- 2025-11-23T18:33:59+00:00: v1.33.6 - https://github.com/Comfy-Org/ComfyUI_frontend/releases/tag/v1.33.6 __auto-added__
- 2025-11-23T18:49:45+00:00: v1.33.7 - https://github.com/Comfy-Org/ComfyUI_frontend/releases/tag/v1.33.7 __auto-added__
- 2025-11-24T06:35:25+00:00: v1.33.8 - https://github.com/Comfy-Org/ComfyUI_frontend/releases/tag/v1.33.8 __auto-added__
- 2025-11-24T06:56:20+00:00: [fix] Fixes non-async public API access (#10857) - https://github.com/comfyanonymous/ComfyUI/commit/f66183a54142be693ab858e9f1f06ed62439a92e __auto-added__
- 2025-11-24T17:48:37+00:00: fix(api-nodes): edge cases in responses for Gemini models (#10860) - https://github.com/comfyanonymous/ComfyUI/commit/3bd71554a2df14b862cc5e1e875df37ba24af1ac __auto-added__
- 2025-11-24T18:40:09+00:00: block info (#10844) - https://github.com/comfyanonymous/ComfyUI/commit/b2ef58e2b17e73ca8cd376a1cdc976518ebbc168 __auto-added__
- 2025-11-24T21:29:13+00:00: HunyuanVideo 1.5 Native Support in ComfyUI - https://blog.comfy.org/p/hunyuanvideo-15-native-support __auto-added__
- 2025-11-25T00:45:54+00:00: Bump transformers version in requirements.txt (#10869) - https://github.com/comfyanonymous/ComfyUI/commit/22a2644e57530ee40e13486ccd7c953b87072093 __auto-added__
- 2025-11-25T06:48:53+00:00: Cleanup and fix issues with text encoder quants. (#10872) - https://github.com/comfyanonymous/ComfyUI/commit/25022e0b0965975b35bcaf28b153184d60a4f9de __auto-added__
- 2025-11-25T07:55:49+00:00: Don't try fp8 matrix mult in quantized ops if not supported by hardwa… - https://github.com/comfyanonymous/ComfyUI/commit/acfaa5c4a132e1c01bc9d94e76b0d667c899bfd1 __auto-added__
- 2025-11-25T08:23:19+00:00: I found a case where this is needed (#10875) - https://github.com/comfyanonymous/ComfyUI/commit/015a0599d08f1072155b9213d488b73e502fea3c __auto-added__
- 2025-11-25T14:10:51+00:00: Comfy Cloud: new features and pricing changes - https://blog.comfy.org/p/comfy-cloud-new-features-and-pricing __auto-added__
- 2025-11-25T15:50:19+00:00: Flux 2 (#10879) - https://github.com/comfyanonymous/ComfyUI/commit/6b573ae0cb11000a0330a35d9e31917c22c874a4 __auto-added__
- 2025-11-25T16:09:07+00:00: [API Nodes] add Flux.2 Pro node (#10880) - https://github.com/comfyanonymous/ComfyUI/commit/5c7b08ca58f5412b3a814b374793cacdb5b5f0a7 __auto-added__
- 2025-11-25T16:40:32+00:00: Add Flux 2 support to README. (#10882) - https://github.com/comfyanonymous/ComfyUI/commit/af81cb962d9dd283ddb551962cc223b5a186a1ce __auto-added__
- 2025-11-25T17:40:58+00:00: ComfyUI version v0.3.72 - https://github.com/comfyanonymous/ComfyUI/commit/828b1b9953175b6df79459f417d1032869d0b46a __auto-added__
- 2025-11-25T17:40:58+00:00: v0.3.72 - https://github.com/comfyanonymous/ComfyUI/releases/tag/v0.3.72 __auto-added__
- 2025-11-25T19:18:51+00:00: FLUX.2 Day-0 Support in ComfyUI: Frontier Visual Intelligence - https://blog.comfy.org/p/flux2-state-of-the-art-visual-intelligence __auto-added__
- 2025-11-25T19:30:24+00:00: Fix crash. (#10885) - https://github.com/comfyanonymous/ComfyUI/commit/dff996ca39d86265bbabf15e666484e051f0b3d5 __auto-added__
- 2025-11-25T19:59:37+00:00: ComfyUI v0.3.73 - https://github.com/comfyanonymous/ComfyUI/commit/0c18842acbdf546883b08808dd9feea7605d7649 __auto-added__
- 2025-11-25T19:59:37+00:00: v0.3.73 - https://github.com/comfyanonymous/ComfyUI/releases/tag/v0.3.73 __auto-added__
- 2025-11-25T20:51:37+00:00: v0.5.9 - https://github.com/Comfy-Org/desktop/releases/tag/v0.5.9 __auto-added__
- 2025-11-25T23:27:15+00:00: v0.5.10 - https://github.com/Comfy-Org/desktop/releases/tag/v0.5.10 __auto-added__
- 2025-11-25T23:41:45+00:00: Z Image model. (#10892) - https://github.com/comfyanonymous/ComfyUI/commit/e9aae31fa241a6a63a368800146ea91629d4e8c2 __auto-added__
- 2025-11-26T00:02:51+00:00: Adjustments to Z Image. (#10893) - https://github.com/comfyanonymous/ComfyUI/commit/0e24dbb19f34f242edb77c550396cf6806f7b22f __auto-added__
- 2025-11-26T00:01:15+00:00: v1.33.9 - https://github.com/Comfy-Org/ComfyUI_frontend/releases/tag/v1.33.9 __auto-added__
- 2025-11-26T01:10:51+00:00: v1.32.9 - https://github.com/Comfy-Org/ComfyUI_frontend/releases/tag/v1.32.9 __auto-added__
- 2025-11-26T05:07:58+00:00: Fix loras not working on mixed fp8. (#10899) - https://github.com/comfyanonymous/ComfyUI/commit/bdb10a583f1b1e495ee00dbd1674f11016a6a93e __auto-added__
- 2025-11-26T05:34:15+00:00: ComfyUI v0.3.74 - https://github.com/comfyanonymous/ComfyUI/commit/90b3995ec842335e44d70e0521ff6ff6c3ff9aaa __auto-added__
- 2025-11-26T05:34:15+00:00: v0.3.74 - https://github.com/comfyanonymous/ComfyUI/releases/tag/v0.3.74 __auto-added__
- 2025-11-26T07:41:13+00:00: ComfyUI version v0.3.75 - https://github.com/comfyanonymous/ComfyUI/commit/8402c8700a29a97bc5d706d6a0b14c41bc2c2d8a __auto-added__
- 2025-11-26T07:41:13+00:00: v0.3.75 - https://github.com/comfyanonymous/ComfyUI/releases/tag/v0.3.75 __auto-added__
- 2025-11-26T09:00:43+00:00: Add cheap latent preview for flux 2. (#10907) - https://github.com/comfyanonymous/ComfyUI/commit/f16219e3aadcb7a301a1a313ab8989c3ebe53764 __auto-added__
- 2025-11-26T17:23:14+00:00: improve UX for batch uploads in upload_images_to_comfyapi (#10913) - https://github.com/comfyanonymous/ComfyUI/commit/1105e0d139001ad602d0f883406bfce41e54ae67 __auto-added__
- 2025-11-26T18:38:30+00:00: fix(gemini): use first 10 images as fileData (URLs) and remaining ima… - https://github.com/comfyanonymous/ComfyUI/commit/8908ee262862f1252d1363d55c59872fb3361066 __auto-added__
- 2025-11-26T19:26:37+00:00: v1.34.0 - https://github.com/Comfy-Org/ComfyUI_frontend/releases/tag/v1.34.0 __auto-added__
- 2025-11-26T19:58:27+00:00: Merge 3d animation node (#10025) - https://github.com/comfyanonymous/ComfyUI/commit/58c6ed541d5aaf6d9b12f63bc23c33164e1cf7a3 __auto-added__
- 2025-11-26T20:16:40+00:00: Fix the CSP offline feature. (#10923) - https://github.com/comfyanonymous/ComfyUI/commit/55f654db3ddaf5a10ac6dbe79774c23c350d279d __auto-added__
- 2025-11-26T20:36:38+00:00: Add Z Image to readme. (#10924) - https://github.com/comfyanonymous/ComfyUI/commit/dd41b745497cdbbafb0bd745f590726b0e41f9f3 __auto-added__
- 2025-11-26T22:00:40+00:00: v0.5.11 - https://github.com/Comfy-Org/desktop/releases/tag/v0.5.11 __auto-added__
- 2025-11-26T22:42:01+00:00: chore(api-nodes): remove chat widgets from OpenAI/Gemini nodes (#10861) - https://github.com/comfyanonymous/ComfyUI/commit/d8433c63fdacef24f40da401b02ebba272bf1fbb __auto-added__
- 2025-11-26T22:55:31+00:00: convert nodes_customer_sampler.py to V3 schema (#10206) - https://github.com/comfyanonymous/ComfyUI/commit/a2d60aad0f8e03657d501842460123f6eaaf6791 __auto-added__
- 2025-11-27T00:25:32+00:00: Make lora training work on Z Image and remove some redundant nodes. (… - https://github.com/comfyanonymous/ComfyUI/commit/eaf68c9b5bbfbcdac8988741f3948678c9465c1d __auto-added__
- 2025-11-27T00:32:19+00:00: cloud/v1.33.9: [backport cloud/1.33] feat: open template via URL in linear mode (#6968) - https://github.com/Comfy-Org/ComfyUI_frontend/releases/tag/cloud%2Fv1.33.9 __auto-added__
- 2025-11-27T00:20:57+00:00: Topaz's Flagship Upscale Models in ComfyUI - https://blog.comfy.org/p/topazs-flagship-upscale-models-in __auto-added__
- 2025-11-27T04:28:44+00:00: block info (#10841) - https://github.com/comfyanonymous/ComfyUI/commit/c38e7d6599be1bdce580ccfdbb20b928315af05e __auto-added__
- 2025-11-27T06:03:03+00:00: Account for the VRAM cost of weight offloading (#10733) - https://github.com/comfyanonymous/ComfyUI/commit/f17251bec65b5760cfedec29eace7d77f4b35130 __auto-added__
- 2025-11-27T16:06:30+00:00: quant ops: Dequantize weight in-place (#10935) - https://github.com/comfyanonymous/ComfyUI/commit/3f382a4f9884f7b672557028adb9bb85d075820d __auto-added__
- 2025-11-27T20:09:08+00:00: v1.34.1 - https://github.com/Comfy-Org/ComfyUI_frontend/releases/tag/v1.34.1 __auto-added__
- 2025-11-27T20:27:27+00:00: Z-Image Turbo in ComfyUI: Realism at Lightning Speed - https://blog.comfy.org/p/z-image-turbo-in-comfyui-realism __auto-added__
- 2025-11-27T22:12:56+00:00: Update template to 0.7.23 (#10949) - https://github.com/comfyanonymous/ComfyUI/commit/b59750a86a4687056528f1d59470e207063a73a3 __auto-added__
- 2025-11-27T22:46:12+00:00: Enable async offloading by default on Nvidia. (#10953) - https://github.com/comfyanonymous/ComfyUI/commit/9d8a817985bb069685e440b38762f95dc834d242 __auto-added__
- 2025-11-27T23:40:30+00:00: v1.34.2 - https://github.com/Comfy-Org/ComfyUI_frontend/releases/tag/v1.34.2 __auto-added__
- 2025-11-28T10:52:59+00:00: feat(Kling-API-Nodes): add v2-5-turbo model to FirstLastFrame node (#… - https://github.com/comfyanonymous/ComfyUI/commit/52e778fff3c1d6f32c8d14cba9864faddba8475d __auto-added__
- 2025-11-28T20:43:17+00:00: fix(user_manager): fix typo in move_userdata dest validation (#10967) - https://github.com/comfyanonymous/ComfyUI/commit/ca7808f240d4d53e594d3b95753240313864c992 __auto-added__
- 🔥 2025-11-28T21:16:46+00:00: Disable offload stream when torch compile. (#10961) - https://github.com/comfyanonymous/ComfyUI/commit/f55c98a89f76fc06c435a728bc2e76b6b4051463 __priority-auto-added__
- 2025-11-28T21:33:07+00:00: fix QuantizedTensor.is_contiguous (#10956) (#10959) - https://github.com/comfyanonymous/ComfyUI/commit/6484ac89dc683b178d9ef3f7406800f7132147ba __auto-added__
- 2025-11-28T21:38:12+00:00: mm: wrap the raw stream in context manager (#10958) - https://github.com/comfyanonymous/ComfyUI/commit/0ff0457892467ef8a6ea235dcd0618c10ca44ee3 __auto-added__
- 2025-11-29T00:40:19+00:00: Support video tiny VAEs (#10884) - https://github.com/comfyanonymous/ComfyUI/commit/b9070857092a78cc952d70025fdcc0ff540d96ec __auto-added__
- 2025-11-29T02:12:42+00:00: Support some z image lora formats. (#10978) - https://github.com/comfyanonymous/ComfyUI/commit/52a32e2b323b90295ab05a8c299590c890f2ecb6 __auto-added__
- 🔥 2025-11-29T02:28:42+00:00: feat(security): add System User protection with `__` prefix (#10966) - https://github.com/comfyanonymous/ComfyUI/commit/af96d9812de3e420abd43275d9a5960535b6333c __priority-auto-added__
- 2025-11-29T04:55:00+00:00: Add some missing z image lora layers. (#10980) - https://github.com/comfyanonymous/ComfyUI/commit/5151cff293607c2191981fd16c62c1b1a6939695 __auto-added__
- 2025-11-29T23:00:55+00:00: Make the ScaleRope node work on Z Image and Lumina. (#10994) - https://github.com/comfyanonymous/ComfyUI/commit/0a6746898d6864d65e2fc7504e5e875f8c19c0ba __auto-added__
- 2025-11-30T02:07:26+00:00: update template to 0.7.25 (#10996) - https://github.com/comfyanonymous/ComfyUI/commit/4967f81778f84b41acc40ed03536dd71dd88e5f2 __auto-added__
- 2025-11-30T03:28:42+00:00: Echoes of Time: Lighting Up a Historic Fortress with ComfyUI - https://blog.comfy.org/p/echoes-of-time-lighting-up-a-historic __auto-added__
- 🔥 2025-11-30T09:21:31+00:00: Next AMD portable will have pytorch with ROCm 7.1.1 (#11002) - https://github.com/comfyanonymous/ComfyUI/commit/f8b981ae9a5676311624bbafa636a1874db79459 __priority-auto-added__
- 2025-12-01T06:50:42+00:00: v1.34.3 - https://github.com/Comfy-Org/ComfyUI_frontend/releases/tag/v1.34.3 __auto-added__
- 2025-12-01T18:27:17+00:00: bump comfyui-frontend-package to 1.32.10 (#11018) - https://github.com/comfyanonymous/ComfyUI/commit/7dbd5dfe91f057b83dcba0c127f712f6d71f7def __auto-added__
- 2025-12-01T22:13:48+00:00: Update qwen tokenizer to add qwen 3 tokens. (#11029) - https://github.com/comfyanonymous/ComfyUI/commit/2640acb31ccfddee57ba22d5245bf456e8dffe53 __auto-added__
- 2025-12-02T00:11:52+00:00: [API Nodes] add Kling O1 model support (#11025) - https://github.com/comfyanonymous/ComfyUI/commit/1cb7e22a95701f2619d1ddf5683ea221b58a0c13 __auto-added__
- 2025-12-02T01:56:38+00:00: bump comfyui-frontend-package to 1.33.10 (#11028) - https://github.com/comfyanonymous/ComfyUI/commit/c55dc857d5da5af203caf720ed7056047d382544 __auto-added__
- 2025-12-02T01:25:35+00:00: v0.3.76 - https://github.com/comfyanonymous/ComfyUI/releases/tag/v0.3.76 __auto-added__
- 2025-12-02T03:40:44+00:00: Add @guill as a code owner (#11031) - https://github.com/comfyanonymous/ComfyUI/commit/a17cf1c3871ad582c85c2bb6fddb63ec9c6df0ce __auto-added__
- 2025-12-02T04:10:54+00:00: v0.5.12 - https://github.com/Comfy-Org/desktop/releases/tag/v0.5.12 __auto-added__
- 2025-12-02T19:46:29+00:00: Fix CODEOWNERS formatting to have all on the same line, otherwise onl… - https://github.com/comfyanonymous/ComfyUI/commit/44baa0b7f32dd0c2ff0a9898aeb6c7929d855cd3 __auto-added__
- 2025-12-02T19:50:13+00:00: add check for the format arg type in VideoFromComponents.save_to func… - https://github.com/comfyanonymous/ComfyUI/commit/33d6aec3b70bc6f3e5bba26c85bd8f3bb1380d08 __auto-added__
- 2025-12-02T22:24:19+00:00: attention: use flag based OOM fallback (#11038) - https://github.com/comfyanonymous/ComfyUI/commit/277237ccc1499bac7fcd221a666dfe7a32ac4206 __auto-added__
- 2025-12-03T02:38:31+00:00: Support Z Image alibaba pai fun controlnets. (#11062) - https://github.com/comfyanonymous/ComfyUI/commit/b94d394a64dd0af06bca44b96c66549bb463331d __auto-added__
- 2025-12-03T02:28:20+00:00: v1.34.4 - https://github.com/Comfy-Org/ComfyUI_frontend/releases/tag/v1.34.4 __auto-added__
- 2025-12-03T03:29:27+00:00: Added PATCH method to CORS headers (#11066) - https://github.com/comfyanonymous/ComfyUI/commit/3f512f5659cfbb3c53999cde6ff557591740252b __auto-added__
- 2025-12-03T03:31:27+00:00: v1.34.5 - https://github.com/Comfy-Org/ComfyUI_frontend/releases/tag/v1.34.5 __auto-added__
- 2025-12-03T03:49:29+00:00: Implement temporal rolling VAE (Major VRAM reductions in Hunyuan and … - https://github.com/comfyanonymous/ComfyUI/commit/73f5649196f472d3719e2e7513e0a9d029cc3e38 __auto-added__
- 2025-12-03T05:02:09+00:00: v0.3.77 - https://github.com/comfyanonymous/ComfyUI/releases/tag/v0.3.77 __auto-added__
- 2025-12-03T05:17:13+00:00: Add MatchType, DynamicCombo, and Autogrow support to V3 Schema (#10832) - https://github.com/comfyanonymous/ComfyUI/commit/c120eee5bacca643062657d2a7efad83c7d4d828 __auto-added__
- 2025-12-03T05:47:51+00:00: Fix issue with portable updater. (#11070) - https://github.com/comfyanonymous/ComfyUI/commit/861817d22d2659099811b56005c9eaea18d64c73 __auto-added__
- 2025-12-03T07:28:45+00:00: Prs/lora reservations (reduce massive Lora reservations especially on… - https://github.com/comfyanonymous/ComfyUI/commit/519c9411653df99761053c30e101816e0ca3c24b __auto-added__
- 2025-12-03T11:02:23+00:00: 5.6.0 - https://github.com/runpod-workers/worker-comfyui/releases/tag/5.6.0 __auto-added__
- 2025-12-03T16:37:35+00:00: fix(V3-Schema): use empty list defaults for Schema.inputs/outputs/hid… - https://github.com/comfyanonymous/ComfyUI/commit/19f2192d69d13445131b72ad1d87167f59b66fc4 __auto-added__
- 2025-12-03T16:55:44+00:00: add support for "@image" reference format in Kling Omni API nodes (#1… - https://github.com/comfyanonymous/ComfyUI/commit/87c104bfc1928f0b018a50f5867f425e10482929 __auto-added__
- 2025-12-03T21:52:31+00:00: convert nodes_load_3d.py to V3 schema (#10990) - https://github.com/comfyanonymous/ComfyUI/commit/440268d3940eb14a01595439bbc05c4aacde9c72 __auto-added__
- 2025-12-04T01:35:04+00:00: convert nodes_audio.py to V3 schema (#10798) - https://github.com/comfyanonymous/ComfyUI/commit/dce518c2b4f99634b5fdde1924d9b0bd468fe1ce __auto-added__
- 2025-12-04T04:15:15+00:00: Fix case where text encoders where running on the CPU instead of GPU.… - https://github.com/comfyanonymous/ComfyUI/commit/ea17add3c62197b10fd0b71d9169d339adc55c47 __auto-added__
- 2025-12-04T04:28:44+00:00: mp: use look-ahead actuals for stream offload VRAM calculation (#11096) - https://github.com/comfyanonymous/ComfyUI/commit/6be85c7920224b45bbc6417e00147815e78c12a9 __auto-added__
- 2025-12-04T08:33:08+00:00: v1.34.6 - https://github.com/Comfy-Org/ComfyUI_frontend/releases/tag/v1.34.6 __auto-added__
- 2025-12-04T17:50:36+00:00: sd: bump HY1.5 VAE estimate (#11107) - https://github.com/comfyanonymous/ComfyUI/commit/9bc893c5bbd2838bdd15ebd40e3a3e548ce3e4f0 __auto-added__
- 2025-12-04T22:05:28+00:00: [API Nodes]: fixes and refactor (#11104) - https://github.com/comfyanonymous/ComfyUI/commit/3c8456223c5f6a41af7d99219b391c8c58acb552 __auto-added__
- 2025-12-05T00:22:06+00:00: Try Nodes 2.0 And Help Us Improve ComfyUI! - https://blog.comfy.org/p/comfyui-node-2-0 __auto-added__
- 2025-12-05T03:52:09+00:00: Forgot to put this in README. (#11112) - https://github.com/comfyanonymous/ComfyUI/commit/35fa091340c60612dfb71cb6822dc23b99a5dac2 __auto-added__
- 2025-12-05T19:05:38+00:00: Remove line made unnecessary (and wrong) after transformer_options wa… - https://github.com/comfyanonymous/ComfyUI/commit/0ec05b1481d12b299bc945dbd407b773cfb66483 __auto-added__
- 2025-12-05T19:35:42+00:00: Make old scaled fp8 format use the new mixed quant ops system. (#11000) - https://github.com/comfyanonymous/ComfyUI/commit/43071e3de3780f984a46549e90935a0bf405e9df __auto-added__
- 2025-12-05T20:33:16+00:00: Fix regression when text encoder loaded directly on GPU. (#11129) - https://github.com/comfyanonymous/ComfyUI/commit/6fd463aec958f02be79a264eafd6c8fe7e52762a __auto-added__
- 2025-12-05T20:42:46+00:00: Context windows fixes and features (#10975) - https://github.com/comfyanonymous/ComfyUI/commit/79d17ba2339aaf4f3422673b3dad24ba4dbd7552 __auto-added__
- 2025-12-05T23:25:31+00:00: Fix some custom nodes. (#11134) - https://github.com/comfyanonymous/ComfyUI/commit/092ee8a5008c8d558b0a72cc7961a31d9cc5400b __auto-added__
- 2025-12-05T23:45:38+00:00: docs: add ComfyUI-Manager documentation and update to v4.0.3b4 (#11133) - https://github.com/comfyanonymous/ComfyUI/commit/bed12674a1d2c4bfdfbdd098686390f807996c90 __auto-added__
- 2025-12-06T03:20:22+00:00: Kandinsky5 model support (#10988) - https://github.com/comfyanonymous/ComfyUI/commit/fd109325db7126f92c2dfb7e6b25310eded8c1f8 __auto-added__
- 2025-12-06T04:01:19+00:00: Fix regression. (#11137) - https://github.com/comfyanonymous/ComfyUI/commit/ae676ed105663bb225153c8bca406f00edf738b4 __auto-added__
- 2025-12-06T04:24:10+00:00: [V3] convert nodes_mask.py to V3 schema (#10669) - https://github.com/comfyanonymous/ComfyUI/commit/913f86b72740f84f759786a698108840a09b6498 __auto-added__
- 2025-12-06T05:15:21+00:00: Set OCL_SET_SVM_SIZE on AMD. (#11139) - https://github.com/comfyanonymous/ComfyUI/commit/d7a0aef65033bf0fe56e521577a44fac1830b8b3 __auto-added__
- 2025-12-06T11:28:08+00:00: marked all Pika API nodes a deprecated (#11146) - https://github.com/comfyanonymous/ComfyUI/commit/76f18e955dcbc88ed13d6802194fd897927f93e5 __auto-added__
- 2025-12-06T18:09:44+00:00: Fix EmptyAudio node input types (#11149) - https://github.com/comfyanonymous/ComfyUI/commit/7ac7d69d948e75c3a230d1262daab84d75aff895 __auto-added__
- 2025-12-06T23:36:20+00:00: Speed up lora compute and lower memory usage by doing it in fp16. (#1… - https://github.com/comfyanonymous/ComfyUI/commit/50ca97e7765d9bbdbeec31a75f1f6c747d76948c __auto-added__
- 2025-12-06T23:42:09+00:00: Fix on-load VRAM OOM (#11144) - https://github.com/comfyanonymous/ComfyUI/commit/4086acf3c2f0ca3a8861b04f6179fa9f908e3e25 __auto-added__
- 2025-12-07T01:50:10+00:00: Fix qwen scaled fp8 not working with kandinsky. Make basic t2i wf wor… - https://github.com/comfyanonymous/ComfyUI/commit/329480da5ab32949a411548f821ea60ab3e90dc7 __auto-added__
- 2025-12-07T12:44:55+00:00: Properly load the newbie diffusion model. (#11172) - https://github.com/comfyanonymous/ComfyUI/commit/56fa7dbe380cb5591c5542f8aa51ce2fc26beedf __auto-added__
- 2025-12-07T15:45:44+00:00: Kling O1 in ComfyUI: The Video Editing Era - https://blog.comfy.org/p/kling-o1-in-comfyui-the-video-editing __auto-added__
- 2025-12-08T09:33:46+00:00: [API Nodes] add support for seedance-1-0-pro-fast model (#10947) - https://github.com/comfyanonymous/ComfyUI/commit/fd271dedfde6e192a1f1a025521070876e89e04a __auto-added__
- 2025-12-08T20:18:53+00:00: chore: update workflow templates to v0.7.54 (#11192) - https://github.com/comfyanonymous/ComfyUI/commit/935493f6c186de8808508713a465d6bda75e5ce4 __auto-added__
- 2025-12-08T22:38:36+00:00: Fix regression. (#11194) - https://github.com/comfyanonymous/ComfyUI/commit/3b0368aa34182fc7c97de92d59b609c77138def2 __auto-added__
- 2025-12-08T23:27:45+00:00: v1.34.7 - https://github.com/Comfy-Org/ComfyUI_frontend/releases/tag/v1.34.7 __auto-added__
- 2025-12-09T03:24:23+00:00: v1.35.0 - https://github.com/Comfy-Org/ComfyUI_frontend/releases/tag/v1.35.0 __auto-added__
- 2025-12-09T04:21:31+00:00: dequantization offload accounting (fixes Flux2 OOMs - incl TEs) (#11171) - https://github.com/comfyanonymous/ComfyUI/commit/e136b6dbb0b08341388f5bf9a00b1fca29992eb3 __auto-added__
- 2025-12-09T04:33:29+00:00: add chroma-radiance-x0 mode (#11197) - https://github.com/comfyanonymous/ComfyUI/commit/b9fb542703085c58f082b4a822329fb6670e8016 __auto-added__
- 2025-12-09T05:55:13+00:00: ops: delete dead code (#11204) - https://github.com/comfyanonymous/ComfyUI/commit/9d252f3b70c0e89cbb581e28bb1862593c4e5ceb __auto-added__
- 2025-12-09T18:29:05+00:00: Ubisoft Open-Sources the CHORD Model and ComfyUI Nodes for End-to-End PBR Material Generation - https://blog.comfy.org/p/ubisoft-open-sources-the-chord-model __auto-added__
- 2025-12-09T22:03:21+00:00: Fix nan issue when quantizing fp16 tensor. (#11213) - https://github.com/comfyanonymous/ComfyUI/commit/791e30ff5037fa5e7aa4e1396099ea8d6bfb020b __auto-added__
- 2025-12-09T23:26:49+00:00: ComfyUI version v0.4.0 - https://github.com/comfyanonymous/ComfyUI/commit/fc657f471a29d07696ca16b566000e8e555d67d1 __auto-added__
- 2025-12-09T23:26:49+00:00: ComfyUI version v0.4.0 - https://github.com/comfyanonymous/ComfyUI/releases/tag/v0.4.0 __auto-added__
- 2025-12-10T00:58:01+00:00: v1.33.14 - https://github.com/Comfy-Org/ComfyUI_frontend/releases/tag/v1.33.14 __auto-added__
- 2025-12-10T03:27:07+00:00: bump comfyui-frontend-package to 1.34.8 (#11220) - https://github.com/comfyanonymous/ComfyUI/commit/f668c2e3c99df40561b416cf62b0fd9eec96007a __auto-added__
- 2025-12-10T04:26:24+00:00: v0.6.0 - https://github.com/Comfy-Org/desktop/releases/tag/v0.6.0 __auto-added__
- 2025-12-10T10:01:35+00:00: v1.34.8 - https://github.com/Comfy-Org/ComfyUI_frontend/releases/tag/v1.34.8 __auto-added__
- 2025-12-10T10:44:23+00:00: v1.35.1 - https://github.com/Comfy-Org/ComfyUI_frontend/releases/tag/v1.35.1 __auto-added__
- 2025-12-10T19:55:09+00:00: process the NodeV1 dict results correctly (#11237) - https://github.com/comfyanonymous/ComfyUI/commit/36357bbcc3c515e37a742457a2b2ab4b7ccc17a8 __auto-added__
- 2025-12-11T00:59:48+00:00: Tweak Z Image memory estimation. (#11254) - https://github.com/comfyanonymous/ComfyUI/commit/17c92a9f2843d7b9b727531066be2378b350a6ae __auto-added__
- 2025-12-11T02:49:49+00:00: Fix: filter hidden files from /internal/files endpoint (#11191) - https://github.com/comfyanonymous/ComfyUI/commit/57ddb7fd13d817e7259c2c992a852832b6b0f07a __auto-added__
- 2025-12-11T03:02:26+00:00: Lower VAE loading requirements：Create a new branch for GPU memory cal… - https://github.com/comfyanonymous/ComfyUI/commit/e711aaf1a75120195c56ebd1f1ce829c6b7b84db __auto-added__
- 2025-12-11T06:11:12+00:00: feat(api-nodes): enable Kling Omni O1 node (#11229) - https://github.com/comfyanonymous/ComfyUI/commit/93948e3fc598c14082f744fe82fae056b64ff481 __auto-added__
- 2025-12-11T06:30:31+00:00: Adjust memory usage factor. (#11257) - https://github.com/comfyanonymous/ComfyUI/commit/f8321eb57b29a4b34cecd27d5d6365adf5e6e601 __auto-added__
- 2025-12-11T11:15:34+00:00: v1.35.2 - https://github.com/Comfy-Org/ComfyUI_frontend/releases/tag/v1.35.2 __auto-added__
- 2025-12-11T22:09:35+00:00: Fix regular chroma radiance (#11276) - https://github.com/comfyanonymous/ComfyUI/commit/fdebe182966d1dd9bee3138264937137bd2302d8 __auto-added__