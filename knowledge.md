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