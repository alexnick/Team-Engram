# Changelog

All notable changes to Team Engram are recorded here. The project is pre-release; earlier product work is summarized without assigning unsupported release dates.

## Unreleased

### Added

- English, zero-experience task guides for Cursor setup, attached projects, Ask, Add or Update, Ingest, Audit, shared skills, Publish, Merge, local update, conflicts, abandonment or recovery, and terminology.
- A tracked multi-root Cursor workspace example paired with a gitignored local workspace file.
- A GitLab Merge Request template for focused, locally validated changes.
- GitLab-oriented self-merge, synchronization, and recovery guidance with concrete Cursor prompts.

### Changed

- Reframed the product as Team Engram: a shared organizational knowledge corpus rather than a personal Brain.
- Reduced the starter corpus to Knowledge, Decisions, Sources/Raw, Sources/Records, corpus Context, and a locally generated Index.
- Made `.agents/skills/` the canonical location for shared reusable skills; project-only skills remain in project repositories.
- Established Cursor as the primary interface and Team Engram as the stable root of a local multi-root workspace.
- Replaced automatic or implicit publication with a two-boundary flow: local preparation, then explicit `Publish this change` confirmation for commit, push, and GitLab Merge Request creation or update. Merge remains separately human-triggered.
- Defined local validation, optional peer review, squash self-merge, and branch cleanup without GitLab CI or pipelines.
- Allowed complete article-scale text, including multi-screen Confluence articles, to be preserved incrementally as Markdown snapshots while large or binary artifacts remain external.
- Made `CONTEXT-MAP.md` the committed router and `Engram/INDEX.md` deterministic, local, generated, and gitignored.
- Replaced duplicated operation history with Git commits and GitLab Merge Requests.
- Rewrote README, Quickstart, User Guide, Context Map, corpus Context, and public documentation for the shared pilot.

### Removed

- Personal, Health, Inbox, Entities, Events, Sessions, Learning, Feedback, Dashboard, review-state, and internal Project starter areas.
- Capture, Review, Checkpoint, Teach, and product/private synchronization guidance from the Team Engram path.
- The append-only `Engram/LOG.md` and committed generated Index.
- Predefined domains, personal examples, and assumptions that a repository user has a privileged ownership role.
- GitLab CI, pipelines, required status checks, mandatory review, and automatic merge from the pilot design.

## Previous public Engram work

### Added

- Markdown-first durable knowledge with raw and derived source separation.
- Ingest, Query, Sync, Lint, Project Map, Explore, Grilling, and skill-authoring workflows.
- Templates, deterministic local tooling, agent instructions, and MIT licensing.

### Changed

- Renamed the earlier product from Life Workspace to Engram and standardized `Engram/`, `Tools/engram.py`, and English public artifacts.
- Consolidated onboarding and documented product/private maintenance boundaries before the Team Engram fork.

- # Проект: AI-native система автоматизации разработки слот-игр

Я хочу спроектировать внутреннюю систему/платформу, которая максимально автоматизирует производство слот-игр с использованием LLM, coding agents, subagents, skills, deterministic tooling, накопленной кодовой базы компании и внутренних знаний.

Это пока исследовательский проект. Я не хочу заранее привязываться к конкретному harness, базе данных, RAG-фреймворку или агентной архитектуре. Мне важно сначала правильно сформулировать саму задачу и понять, какая архитектура действительно позволит получить большой выигрыш в производительности.

Мне нужен собеседник, который будет критически размышлять вместе со мной, предлагать альтернативные архитектуры и не пытаться автоматически сводить всё к очередному RAG, MCP или swarm из агентов.

---

# 1. Контекст компании и производства

Компания много лет занимается разработкой слот-игр.

Для новых игр используется внутренний TypeScript framework.

Этот framework уже предоставляет примерно 80% стандартной функциональности слот-игры и содержит большое количество внутренних библиотек и абстракций.

Большая часть каждой новой игры состоит из комбинации:

* стандартного framework;
* конфигураций;
* reel configuration;
* ресурсов;
* анимаций;
* UI;
* sounds;
* стандартных игровых состояний;
* integration boilerplate;
* специфичных игровых механик.

При этом игры отличаются не только визуально.

Есть понятие **feature** — дополнительная игровая механика.

Например:

* free spins;
* respins;
* sticky/expanding/walking wild;
* multipliers;
* дополнительные игровые режимы;
* bonus games;
* mini-games;
* специальные reel mechanics;
* различные модификации стандартного gameplay;
* комбинации нескольких механик.

Именно набор features + визуальный стиль во многом делает игру уникальной.

Также существует понятие **reskin**:

одна и та же игра с практически неизменной gameplay logic получает другие assets/theme/presentation.

---

# 2. Текущая экономика производства

Сейчас создание одной игры занимает примерно полгода.

С внедрением AI management ожидает потенциальное сокращение времени разработки примерно в 2–4 раза.

При этом в производстве игры много работы, которая практически механическая:

* создание project structure;
* настройка framework;
* integration assets;
* настройка reels;
* конфигурации;
* подключение animations;
* sounds;
* registration различных элементов;
* boilerplate;
* повторяющиеся framework integrations;
* создание стандартных игровых состояний;
* повторение решений из предыдущих проектов.

Эти части потенциально очень хорошо автоматизируются.

---

# 3. Главное преимущество, которое уже есть у компании

За десятки лет разработки накопился огромный объём уже реализованных features.

Есть:

* старые Java-игры;
* современные TypeScript-игры;
* множество поколений framework;
* огромное количество похожих механик;
* вариации одних и тех же механик;
* фактически копии старых features;
* features, которые были взяты за основу и сильно модифицированы;
* bug fixes;
* production-tested implementations.

То есть почти любая новая feature часто оказывается одним из следующих случаев:

1. Такая feature уже существует.
2. Существует почти такая же feature.
3. Существует несколько её вариантов.
4. Новый дизайн является комбинацией уже существующих mechanics.
5. Нужна адаптация старой Java implementation к новому TypeScript framework.
6. Feature действительно новая, но фундамент для неё можно взять из предыдущих игр.

Таким образом, большая часть интеллектуальной собственности компании сейчас существует в виде **исторического зоопарка implementations**, а не в виде единой формализованной библиотеки игровых механик.

---

# 4. Дополнительный источник знаний

В компании уже существует Confluence.

Причём там есть особенно ценный материал:

* страницы с описанием уникальных features;
* объяснение того, как они работают;
* архитектурные детали;
* иногда причины конкретных решений;
* ссылки на игры;
* ссылки на repositories;
* ссылки на конкретные implementations.

Это означает, что у нас уже есть достаточно хорошая человеческая разметка части исторического кода.

Не нужно начинать полностью с автоматического анализа миллионов файлов.

Confluence можно использовать как seed dataset.

---

# 5. Основная задача

Я хочу создать систему, которая сможет использовать:

* все исторические repositories;
* Java code;
* TypeScript code;
* Confluence;
* внутреннюю framework documentation;
* configs;
* tests;
* git history;
* возможно issue trackers;
* возможно design documentation;

чтобы значительно автоматизировать создание новой игры.

Идеальный конечный сценарий выглядит примерно так:

```text
Game Brief / Game Design / Requirements
                  ↓
         понимание требований
                  ↓
      identification существующих
          reusable mechanics
                  ↓
        выбор лучших исторических
           implementations
                  ↓
           создание проекта
                  ↓
          configuration/setup
                  ↓
      adaptation существующих features
                  ↓
       implementation действительно
             нового кода
                  ↓
          integration assets
                  ↓
             validation
                  ↓
              tests
                  ↓
              build
                  ↓
               PR
```

При этом человек остаётся разработчиком системы и контролирует решения там, где это необходимо.

---

# 6. Главная архитектурная гипотеза

Я не хочу строить просто:

> AI, который пишет слот с нуля.

Более интересная модель:

> AI-native factory, которая понимает всю историю созданных компанией игр, умеет определить, какие части новой игры уже существуют, переиспользовать их, адаптировать и генерировать только необходимую разницу.

Очень грубо:

```text
не:

requirements
    ↓
LLM
    ↓
20 000 строк сгенерированного кода


а:

requirements
    ↓
domain understanding
    ↓
existing building blocks
    ↓
existing implementations
    ↓
configuration / adaptation
    ↓
небольшой новый diff
```

---

# 7. Feature Atlas

Одной из ключевых идей является создание **Feature Atlas**.

Feature Atlas — это не просто очередная wiki и не просто vector database.

Это структурированный каталог всех известных игровых механик компании.

Главный сдвиг:

сейчас knowledge скорее организовано:

```text
Game A
  Feature X
  Feature Y

Game B
  Feature X'
  Feature Z

Game C
  Feature X''
```

Feature Atlas переворачивает это:

```text
Feature X
  Game A implementation
  Game B implementation
  Game C implementation

Feature Y
  Game A implementation
  Game K implementation
```

То есть основной объект знания становится **Feature**, а игры становятся примерами её implementations.

---

# 8. Что должно находиться в Feature Atlas

Для каждой feature полезно постепенно иметь информацию примерно такого характера.

## Feature

Например:

```text
Sticky Wild
```

Описание поведения:

> Wild symbol остаётся на определённой позиции между spins.

---

## Feature family

Например:

```text
Persistent Symbols
```

или:

```text
Free Spins
```

---

## Variants

Например Sticky Wild может иметь варианты:

```text
sticky until feature end
sticky for N spins
sticky until retrigger
sticky with multiplier
sticky with progressive multiplier
```

---

## Variation Points

Это потенциально одна из самых важных частей Atlas.

Не просто:

> у нас есть Sticky Wild.

А:

```text
Sticky Wild

wild lifetime:
    current spin
    N spins
    entire feature
    until retrigger

multiplier:
    none
    fixed
    progressive

scope:
    particular reels
    arbitrary positions
    full reel

reset policy:
    feature end
    retrigger
    state transition
```

То есть historical copy-paste постепенно превращается в понимание:

> какие параметры этой механики на самом деле меняются между играми.

---

## Implementations

Например:

```text
Game A
TypeScript
2023

Game B
TypeScript
2025

Game C
Java
2018
```

---

## Recommended / canonical implementation

Важно понимать не только:

> вот 14 implementation одной mechanic.

Но и:

```text
Recommended modern reference:
Game B

Best tested implementation:
Game D

Legacy Java reference:
Game C
```

Это может сначала размечаться разработчиками вручную.

---

## Relationships

Например:

```text
Sticky Wild
    VARIANT_OF
Persistent Symbol

Sticky Wild
    USED_IN
Game A

Game B implementation
    DERIVED_FROM
Game A implementation

Sticky Wild
    COMBINED_WITH
Progressive Multiplier

Sticky Wild
    DEPENDS_ON
Free Spins
```

---

## Source links

Feature должна быть связана с:

* Confluence;
* repository;
* конкретными files/classes;
* configs;
* commits;
* tests;
* related games.

---

# 9. Feature Atlas не обязательно является сложной БД

Для первого прототипа Atlas вполне может физически существовать как:

```text
feature-atlas/

features/
    sticky-wild.md
    walking-wild.md
    hold-and-win.md
    expanding-wild.md
```

или как Markdown + JSON.

Например карточка:

```text
Sticky Wild

Description:
Wild symbols remain on their positions between spins.

Variants:
- entire feature
- N spins
- progressive multiplier

Implementations:
- Game A
- Game B
- Game C

Recommended:
Game B

Documentation:
Confluence link

Repositories:
...

Known differences:
Game C resets multiplier after retrigger.
```

Это уже Feature Atlas.

База данных, embeddings или knowledge graph могут появиться позже как indexes поверх Atlas.

---

# 10. Как AI должен использовать Feature Atlas

AI не должен каждый раз читать весь Atlas.

Для него должен существовать небольшой domain-specific interface.

Например:

```text
search_features(query)

get_feature(id)

get_implementations(id)
```

Сценарий:

```text
Developer:
"Нужна feature, где wild остаётся между spins
и увеличивает общий multiplier."
```

Agent:

```text
search_features(...)
```

Atlas:

```text
1. Sticky Wild Progressive Multiplier
2. Locked Wild Respins
3. Persistent Wild
```

Agent:

```text
get_feature(sticky-wild-progressive)
```

получает:

```text
behavior
variants
variation points
recommended implementation
related implementations
repository references
```

После этого агент открывает только несколько конкретных исторических implementations.

Таким образом Atlas уменьшает пространство поиска:

```text
весь код компании
       ↓
несколько сотен feature families
       ↓
одна подходящая family
       ↓
несколько implementations
       ↓
конкретные source files
```

Это потенциально гораздо эффективнее, чем просто RAG по всей кодовой базе.

---

# 11. Реализация поиска в Atlas

На первом этапе это не обязательно должно быть сложно.

Можно иметь:

```text
Markdown files
+
index.json
```

В index:

```text
id
name
summary
tags
category
```

Первый `search_features()` может использовать:

* keyword search;
* tags;
* simple text search;
* LLM reranking.

Например:

```text
query
   ↓
keyword/tag search
   ↓
10 candidates
   ↓
LLM semantic reasoning
   ↓
top 3
```

Позже можно добавить:

* embeddings;
* vector search;
* graph search;
* Graphify;
* hybrid retrieval.

Но Atlas должен существовать независимо от конкретной search technology.

---

# 12. Graphify / Graphiti / Knowledge Graph

Knowledge graph потенциально очень хорошо подходит как **индекс поверх Atlas**, потому что здесь естественно существует много relations:

```text
Feature
Variant
Game
Implementation
Framework API
Config
Class
Commit
Bug
Documentation
```

Но важно разделять:

```text
Feature Atlas = знания и domain model

Graphify/Graph DB = способ индексировать и находить связи

LLM = потребитель этих знаний
```

Не хочется получить:

```text
весь корпоративный код
       ↓
Graph database
       ↓
"ну наверное это и есть наши знания"
```

Atlas должен содержать осмысленную инженерную информацию, включая human decisions:

```text
canonical implementation
deprecated implementation
known bad implementation
recommended modern implementation
variation points
```

Автоматический graph extraction сам по себе этого не гарантирует.

---

# 13. GameSpec

Следующая потенциально очень важная концепция — формализованное описание конкретной игры.

Условно:

```yaml
game:
  layout: 5x3

features:
  - type: sticky-wild
    lifetime: feature
    multiplier:
      mode: progressive

  - type: free-spins
    count: 10
    retrigger: true
```

Это не обязательно должен быть YAML.

Смысл в том, чтобы иметь некое **Intermediate Representation игры**.

Как AST у компилятора.

Тогда человеческий game design сначала преобразуется в GameSpec.

---

# 14. Slot Factory как compiler

Одна из главных архитектурных метафор:

```text
Game Requirements
       ↓
LLM / Human
       ↓
GameSpec
       ↓
Feature Resolver
       ↓
Feature Atlas
       ↓
Feature Graph
       ↓
Generators / Adaptation
       ↓
Game project
```

То есть LLM играет роль интеллектуального frontend/compiler planner, а не генератора всей системы.

---

# 15. Deterministic tooling прежде LLM

Очень важный принцип:

> Если задачу можно надёжно решить обычным кодом — не нужно заставлять LLM делать её каждый раз.

Например:

```text
create project
register standard module
copy standard configuration
configure reels
validate assets
generate manifests
create conventional files
run tests
build game
```

должны постепенно превращаться в deterministic tools типа:

```text
game create

game add-feature

game configure-reels

game import-assets

game validate

game test

game build
```

LLM должен решать:

* что вызвать;
* в каком порядке;
* какие параметры использовать;
* какую existing feature выбрать;
* какую implementation взять за reference;
* что необходимо адаптировать.

Но сам boilerplate желательно создавать deterministic способом.

---

# 16. Уровни автоматизации

Полезно классифицировать задачи примерно так:

```text
Reskin
    ↓
почти полностью deterministic

Config-only variation
    ↓
deterministic generation

Existing known feature
    ↓
instantiate/reuse

Existing feature variant
    ↓
reuse + adaptation

Combination of known features
    ↓
integration work

New feature similar to historical feature
    ↓
retrieve nearest implementations + AI adaptation

Actually novel feature
    ↓
developer + AI
```

Система должна пытаться автоматически определить:

> какой минимальный уровень нового engineering необходим для конкретной игры.

---

# 17. Historical Java code

Старый Java code не обязательно воспринимать как legacy junk.

Даже если новые проекты TypeScript, Java implementation может быть хорошим **behavioral reference**.

Например:

```text
New TypeScript task
        ↓

Atlas finds:

Java Game A:
95% behavioral match

TypeScript Game B:
70% behavioral match,
но современная framework architecture
```

Тогда AI может использовать:

```text
Java implementation
для понимания поведения

+

TypeScript implementation
для понимания современной integration architecture
```

---

# 18. Feature lineage / Feature Genome

Ещё одна перспективная идея — восстанавливать происхождение implementations.

Например:

```text
Game A implementation
       ↓ copied
Game B implementation
       ↓ modified
Game C implementation
       ↓ bug fixed
Game D implementation
```

Это можно постепенно извлекать из:

* git history;
* timestamps;
* code similarity;
* class structure;
* commits;
* Confluence;
* LLM analysis.

Тогда вместо 10 независимых implementations система понимает:

> это одно семейство, выросшее из общего предка.

Условно это можно назвать **Feature Genome**.

---

# 19. Автоматическое обнаружение variation points

Особенно интересная задача:

взять несколько похожих implementations одной feature:

```text
Game A
Game B
Game C
Game D
```

и определить:

```text
что invariant
```

против:

```text
что менялось
```

Например:

```text
invariant:
- lifecycle
- framework hooks
- reel state handling

variable:
- multiplier
- reset policy
- affected reels
- retrigger behavior
```

Это может помочь постепенно превращать копипасту из старых games в настоящие reusable parameterized building blocks framework.

---

# 20. Agents

Agents появляются поверх всей этой инфраструктуры.

Не хочется начинать проект с:

```text
20 subagents
```

Более разумный начальный вариант:

```text
Orchestrator

    ├── Research / Archaeology
    ├── Implementation
    └── Verification
```

## Research / Archaeology Agent

Его задача:

* понять requested feature;
* найти Feature Atlas entries;
* найти похожие historical games;
* изучить implementations;
* изучить git history;
* выявить known problems;
* предложить implementation plan.

---

## Implementation Agent

Получает:

```text
GameSpec
Feature Atlas
selected implementation
current project
```

и делает минимальные необходимые изменения.

---

## Verification Agent

Желательно отдельный от implementer.

Он:

* compile;
* lint;
* tests;
* config validation;
* game simulation;
* runtime checks;
* asset validation;
* possibly compare behavior.

---

# 21. Verification особенно важен

Если framework позволяет запускать игры детерминированно по seed или event sequence, появляется очень сильная возможность.

Например для reskin:

```text
Old Game Logic
      ↓
seed 123
      ↓
events/results

New Reskin
      ↓
seed 123
      ↓
events/results
```

Gameplay behavior должен быть identical.

То же может работать для:

* ports;
* feature refactors;
* AI-generated adaptations;
* framework migrations.

Чем лучше automatic verification, тем больше изменений можно безопасно доверять агентам.

---

# 22. Возможная итоговая архитектура

Концептуально:

```text
┌─────────────────────────────────────────────┐
│                 SLOT FACTORY                │
│                                             │
│  KNOWLEDGE                                  │
│                                             │
│  Feature Atlas                              │
│  Feature families                           │
│  Variants                                   │
│  Variation points                           │
│  Feature lineage                            │
│  Games                                      │
│  Code / configs / docs / tests / history    │
│                                             │
├─────────────────────────────────────────────┤
│  DOMAIN                                     │
│                                             │
│  GameSpec                                   │
│  FeatureSpec                                │
│  Feature Graph                              │
│  Compatibility rules                        │
│                                             │
├─────────────────────────────────────────────┤
│  DETERMINISTIC TOOLING                      │
│                                             │
│  Project generator                          │
│  Feature installer                          │
│  Config generators                          │
│  Reel tooling                               │
│  Asset pipeline                             │
│  Build                                      │
│  Tests                                      │
│  Simulation                                 │
│  Validation                                 │
│                                             │
├─────────────────────────────────────────────┤
│  AI / AGENTS                                │
│                                             │
│  Requirement understanding                  │
│  Feature discovery                          │
│  Planning                                   │
│  Adaptation                                 │
│  Implementation                             │
│  Verification                               │
│                                             │
└─────────────────────────────────────────────┘
```

---

# 23. Cursor / existing developer tooling

Не обязательно сразу создавать собственный AI IDE/harness.

Политически и практически хороший первый подход:

```text
Cursor
   ↓
company-specific tools
   ↓
Slot Factory
```

То есть developer продолжает использовать Cursor, но агент получает специальные capabilities:

```text
search_features
inspect_feature
find_similar_games
get_implementation
compare_implementations
create_game
add_feature
configure_reels
validate_game
run_tests
build_game
```

Для самого первого прототипа они могут быть даже обычным CLI:

```text
slot search-feature "sticky wild multiplier"

slot feature sticky-wild

slot implementations sticky-wild
```

Cursor умеет запускать shell.

MCP можно добавить позже как красивый typed interface.

---

# 24. Cordis

Cordis рассматривался как потенциальный framework для будущего custom harness.

Он может быть полезен позже для:

* plugin architecture;
* dependency injection;
* tool lifecycle;
* service composition;
* multiple agents;
* capability isolation;
* different providers;
* hot-swappable services.

Например:

```text
FeatureAtlasService
RepositoryService
GameSpecService
BuildService
TestService
AgentService
```

Но Cordis НЕ является фундаментальной частью идеи.

Если Cordis завтра исчезнет, основная ценность проекта должна сохраниться:

```text
Feature Atlas
GameSpec
Feature ontology
Feature lineage
Variation points
Generators
Validators
Evaluation dataset
```

Поэтому не нужно начинать implementation с Cordis.

---

# 25. Как я представляю первый MVP

Не пытаться сразу индексировать все десятилетия компании.

Взять небольшой vertical slice.

Например:

```text
10–20 хорошо известных features

несколько десятков игр

Confluence pages

linked repositories
```

Создать вручную/полуавтоматически Feature Atlas.

Для каждой feature:

```text
name
description
family
variants
variation points
implementations
recommended implementation
Confluence links
repo links
```

После этого сделать первый полезный инструмент:

```text
search_features(query)
```

Например:

```text
"wild remains after spin and multiplier increases"
```

должен вернуть:

```text
Sticky Wild Progressive Multiplier

Best implementation:
Game A

Alternative:
Game B

Legacy Java reference:
Game C
```

А дальше developer/agent может открыть конкретный код.

---

# 26. Следующий MVP

После работающего Feature Atlas:

```text
Developer:
"Добавь такую же mechanic в текущую игру,
но multiplier должен reset после retrigger."
```

System:

```text
understands request
       ↓
searches Atlas
       ↓
finds closest variant
       ↓
selects canonical implementation
       ↓
compares implementation with current project
       ↓
produces implementation plan
       ↓
makes small code/config diff
       ↓
build
       ↓
tests
```

Если такой сценарий начинает работать стабильно — направление проекта подтверждено.

---

# 27. Evaluation / Benchmark

Я хочу иметь реальный benchmark, а не субъективное ощущение «AI ускоряет».

Для этого можно использовать уже выпущенные игры как historical ground truth.

Берём старую game requirement/design и притворяемся, что готовой игры нет.

Система должна попытаться воспроизвести её development.

Потом сравниваем с реальной implementation.

Возможные метрики:

```text
Feature identification accuracy

Correct historical implementation retrieval

Build success rate

Test pass rate

Number of human corrections

Time to implementation

Generated LOC

Reused LOC

Config reuse

Behavioral equivalence

Number of agent iterations
```

Так можно реально проверить обещания про x2 / x4.

---

# 28. Важные принципы проекта

## 1. Не превращать всё в RAG

RAG по миллионам строк кода может быть одним из search mechanisms, но не domain model.

---

## 2. Не заставлять LLM делать deterministic work

Если operation можно выразить обычной программой — сделать tool.

---

## 3. Retrieval прежде generation

Сначала:

> Делали ли мы это уже?

Потом:

> Что нужно написать нового?

---

## 4. Structured domain knowledge важнее embeddings

Feature / Variant / Implementation / Game / Relation должны существовать как понятные концепции.

---

## 5. Human knowledge является ценным input

Senior developer может сказать:

> implementation из Game X считается плохой.

Это valuable knowledge, которого нет в embeddings.

---

## 6. Sources и provenance

Нужно различать:

```text
machine fact
LLM inference
human verified knowledge
```

Например:

```text
uses SomeFrameworkClass
```

можно определить AST-анализом.

А:

```text
this class controls sticky-wild lifecycle
```

может быть LLM inference.

---

## 7. Не оптимизировать инфраструктуру раньше времени

Первый Atlas может быть Markdown.

Первый search может быть CLI.

Первый agent может быть Cursor.

Ценность проекта должна доказываться до создания большой платформы.

---

# 29. Вопросы, которые я хочу дальше исследовать

Теперь я хочу не просто продолжить описанную архитектуру, а критически перебрать пространство решений.

Помоги мне подумать над следующими вопросами:

### A. Правильная ли вообще центральная идея Feature Atlas?

Есть ли более сильная abstraction для такой задачи?

Например:

* Feature Atlas;
* software product line;
* feature models;
* domain-specific language;
* code genealogy;
* recipe system;
* component registry;
* case-based reasoning;
* combination этих подходов.

---

### B. Как должна выглядеть domain model?

Какие сущности действительно нужны?

Например:

```text
Game
Feature
Feature Family
Variant
Implementation
Variation Point
Framework API
Config
Asset
Relation
```

Что здесь лишнее и чего не хватает?

---

### C. Как автоматически построить Atlas из существующих данных?

У нас есть:

```text
Confluence
Git repositories
Java
TypeScript
configs
tests
git history
```

Какой pipeline лучше?

Что извлекать deterministic/static analysis?

Что поручать LLM?

Что должен подтверждать человек?

---

### D. Насколько глубоко нужно анализировать code?

Возможные уровни:

```text
filesystem
text
AST
imports
class hierarchy
call graph
framework API usage
git history
semantic embeddings
LLM summaries
```

Какой минимальный набор даст максимальную пользу?

---

### E. Нужен ли knowledge graph?

И если нужен:

* Graphify?
* Graphiti?
* Neo4j?
* SQLite?
* обычные JSON/Markdown?
* комбинация?

Когда graph реально даёт преимущество, а когда это overengineering?

---

### F. Как должен выглядеть GameSpec?

Можно ли выразить значительную часть слот-игры declarative способом?

Что должно находиться в spec, а что должно оставаться code?

---

### G. Как строить feature reuse?

Можно ли автоматически обнаруживать:

```text
invariants
variation points
feature families
```

на основе нескольких historical implementations?

---

### H. Какова правильная граница между:

```text
deterministic generator
LLM
coding agent
developer
```

---

### I. Какая agent architecture нужна?

Один сильный agent с tools?

Orchestrator + несколько subagents?

Planner / Researcher / Implementer / Verifier?

Когда subagents реально помогают?

---

### J. Как интегрировать систему в текущий workflow разработчиков?

Варианты:

```text
Cursor + CLI
Cursor + MCP
custom web UI
custom agent harness
IDE extension
combination
```

---

### K. Когда имеет смысл собственный harness?

И если он понадобится:

* строить самим;
* использовать Pi;
* Hermes;
* DeepSeek Harness;
* Cordis;
* LangGraph;
* Mastra;
* что-то другое.

Но harness является вторичным вопросом относительно самой domain platform.

---

### L. Как доказать экономический эффект?

Как построить benchmark, который покажет:

```text
baseline development time

vs

AI-assisted Slot Factory development time
```

и позволит объективно проверить ожидания x2–x4?

---

# 30. Что я хочу получить от дальнейшего обсуждения

Не нужно сразу выдавать окончательную архитектуру.

Я хочу исследовать пространство решений.

Можно:

* критиковать Feature Atlas;
* предлагать альтернативные abstractions;
* сравнивать разные approaches;
* искать слабые места;
* выявлять hidden complexity;
* предлагать incremental MVP;
* рассматривать, что реально можно сделать одному developer внутри компании;
* отделять впечатляющий demo от production platform;
* думать о том, где AI действительно даст multiplicative effect, а где создаст только дополнительную сложность.

Моя конечная цель:

> найти архитектуру внутренней AI-native Slot Development Platform, которая сможет использовать десятилетия накопленного company knowledge и historical implementations для радикального сокращения времени производства новых игр.

Хочу двигаться к этому постепенно, проверяя каждую гипотезу маленькими working prototypes, а не начинать сразу со строительства огромной AI-инфраструктуры.
