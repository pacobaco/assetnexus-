# AssetNexus

AssetNexus is a graph-based search engine for discovering latent and fragmented
assets across accounting systems, infrastructure telemetry, and operational records.

## Features

- Ledger ingestion
- Graph construction using NetworkX
- Asset ranking with PageRank
- Latent asset reconstruction
- Interactive dashboard visualization

## Quick Start

Install dependencies:

pip install -r requirements.txt

Build the graph:

python core/graph_builder.py

Run ranking:

python core/pagerank_ranker.py

Reconstruct asset clusters:

python core/asset_reconstruction.py

Launch dashboard:

python dashboard/dashboard.py