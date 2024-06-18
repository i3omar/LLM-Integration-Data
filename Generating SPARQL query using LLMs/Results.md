# Generating SPARQL query using LLMs

This document provides a list of queries and their outputs that were developed using GPT-4. These queries are tailored to answer a variety of simple questions pertinent to our toolkit, utilizing a complete RDF definition file to guide the model in generating appropriate SPARQL queries. Despite the queries adhering to the correct SPARQL standard format and being informed by the SOSA ontology, which indicated an understanding of the dataset structure, most generated queries failed to retrieve results. Only the first query produced a result that was incorrect. This highlights the model's tendency to replicate the query structure accurately and apply filters effectively, demonstrating strong entity extraction capabilities. However, the results underscore the current limitations of using large language models directly for SPARQL query generation without additional context or data adjustments. This analysis suggests that while direct conversion of end-user queries to SPARQL by LLMs may not yet be robust, these models can still significantly contribute to enhancing data extraction techniques.

## Queries

### 1. Dara's Data Queries
- **1.1** Select Dara's readings value when Dara's speed exceeded 170.
- **1.2** Select all Dara's data when its speed exceeded 170.

### 2. Aqeela's PDOP Query
- Select Aqeela's data when its PDOP value was below 10.

### 3. Sandi's Temperature Query
- Select Sandi's data when temperature measurements are below 28 degrees Celsius.

### 4. Putut's Speed Frequency
- Determine how often Putut's sensor recorded a speed that is between 10 and 20.

### 5. Juling's HDOP Query
- Select all Juling readings where HDOP is not bound to a specific value.

### 6. Juling's GPS Readings
- What readings have been recorded by Juling when the sensor type contains GPS?

### 7. Liun's Directional Data
- Show me the Liun readings from when its direction was towards the north.

### 8. Kuma's Altitude Query
- Are there any readings from Kuma with an altitude greater than 1000 meters?

### 9. Kasih's Time-Bound Data
- Are there any readings from Kasih with a result time between January 5, 2022, and January 6, 2022?

### 10. Juling's HDOP Value
- When was the HDOP value <= 10 for the Juling chip?
