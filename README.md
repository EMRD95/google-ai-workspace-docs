# Google AI Workspace Docs

Corpus compact de documentation officielle sur les outils IA Google / Workspace et quelques intégrations officielles liées.

Le dépôt est volontairement plat : pas d’arborescence de docs, pas de JSON, pas de scripts Python suivis dans git.

## Fichiers

- `llms.txt` — index court / présentation du corpus.
- `llms-full.txt` — corpus complet en un seul fichier, prêt pour ingestion LLM.

## Contenu

`llms-full.txt` regroupe :

- 440 documents sources
- 440 URLs sources conservées
- les titres originaux
- les zones produit / coverage
- le contenu extrait des sources officielles

## Règle de source

Uniquement des sources officielles et traçables.

Sources Google officielles en priorité. Les sources officielles non-Google sont acceptées quand elles documentent directement une intégration ou un usage lié, par exemple draw.io.

Pas de guides synthétiques écrits à la main, pas de billets communautaires, pas de threads, pas de contenu inventé.

## Utilisation

Pour donner tout le contexte à un modèle : utiliser `llms-full.txt`.

Pour comprendre rapidement ce qu’il y a dans le dépôt : lire `llms.txt`.
