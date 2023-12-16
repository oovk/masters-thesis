# Knowledge Base Extraction using LLMs

## Working

- Utilizing Google Gemini in this project.
- Extracting tabular data on the electrical characteristics of electronic components from PDF documents.
- Cleaning the data to ensure it is in the proper format.
- Providing data to the model in CSV format, as the model understands well-formatted data.
- Utilizing prompt engineering to specify the input and output format of the data.
- Extracting triplets containing head, relation, and tail in JSON format using prompts.
- Employing NetworkX and Matplotlib to visualize the knowledge graph.

## Setup

The graph uses relation and entity types from the GENIAL ontology.
[GENIAL Ontology GitHub Repository](https://github.com/wawrzik/GENIALOntologies/tree/master/OntologyModuleSuite/GENIAL!BasicOntology)
