# Generating SPARQL query using LLMs

This document provides a list of queries and their outputs that were developed using GPT-4. These queries are tailored to answer a variety of simple questions pertinent to our toolkit, utilizing a complete RDF definition file to guide the model in generating appropriate SPARQL queries. Despite the queries adhering to the correct SPARQL standard format and being informed by the SOSA ontology, which indicated an understanding of the dataset structure, most generated queries failed to retrieve results. Only the first query produced a result that was incorrect. This highlights the model's tendency to replicate the query structure accurately and apply filters effectively, demonstrating strong entity extraction capabilities. However, the results underscore the current limitations of using large language models directly for SPARQL query generation without additional context or data adjustments. This analysis suggests that while direct conversion of end-user queries to SPARQL by LLMs may not yet be robust, these models can still significantly contribute to enhancing data extraction techniques.

(You can download the excel file from here: [Generating_SPARQL_Results.xls](./Generating_SPARQL_Results.xls))




## Queries

### 1. Dara's Data Queries
- Select Dara's readings value when Dara's speed exceeded 170.
  - **Generated SPARQL Query:**
      ```sparql
      PREFIX sosa: <http://www.w3.org/ns/sosa/>
      PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
      PREFIX : <http://api.stardog.com/>
      
      SELECT ?otherObservation ?property ?value
      WHERE {
        ?speedObservation sosa:madeBySensor <elephant/Dara> ;
                          sosa:observedProperty <property/speed> ;
                          sosa:hasSimpleResult ?speed ;
                          sosa:resultTime ?time .
        FILTER(?speed > 170)
        
        ?otherObservation sosa:madeBySensor <elephant/Dara> ;
                          sosa:resultTime ?time ;
                          sosa:observedProperty ?property ;
                          sosa:hasSimpleResult ?value .
      }
      ```
  - **Result:** Wrong output (incorrect data retrieved)

### 2. Aqeela's PDOP Query
- Select Aqeela's data when its PDOP value was below 10.
  - **Generated SPARQL Query:**
    ```sparql
    PREFIX sosa: <http://www.w3.org/ns/sosa/>
    PREFIX : <http://api.stardog.com/>
    
    SELECT ?observation
    WHERE {
      ?observation sosa:madeBySensor <elephant/Aqeela> ;
                   sosa:observedProperty <property/PDOP> ;
                   sosa:hasSimpleResult ?pdopValue .
      FILTER(?pdopValue < 10)
    }
  
      ```
  - **Result:** No output (query returned no results)
### 3. Sandi's Temperature Query
- Select Sandi's data when temperature measurements are below 28 degrees Celsius.
  - **Generated SPARQL Query:**
    ```sparql
      PREFIX sosa: <http://www.w3.org/ns/sosa/>
      PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
      PREFIX : <http://api.stardog.com/>
      
      SELECT ?observation ?result
      WHERE {
        ?observation sosa:madeBySensor <elephant/Sandi> ;
                     sosa:observedProperty <property/temperature> ;
                     sosa:hasSimpleResult ?result .
        FILTER(?result < 28)
      }
      ```
  - **Result:** No output (query returned no results)
### 4. Putut's Speed Frequency
- Determine how often Putut's sensor recorded a speed that is between 10 and 20.
  - **Generated SPARQL Query:**
    ```sparql
    PREFIX sosa: <http://www.w3.org/ns/sosa/>
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX : <http://api.stardog.com/>
    
    SELECT (COUNT(?observation) as ?numberOfObservations)
    WHERE {
      ?observation sosa:madeBySensor <elephant/Putut> ;
                   sosa:observedProperty <property/speed> ;
                   sosa:hasSimpleResult ?speed .
      FILTER(?speed >= 10 && ?speed <= 20)
    }
      
      ```
  - **Result:** No output (query returned no results)
### 5. Juling's HDOP Query
- Select all Juling readings where HDOP is not bound to a specific value.
  - **Generated SPARQL Query:**
   ```sparql
    PREFIX sosa: <http://www.w3.org/ns/sosa/>
    PREFIX : <http://api.stardog.com/>
    
    SELECT ?observation ?result
    WHERE {
      ?observation sosa:madeBySensor <python/Juling> ;
                   sosa:hasSimpleResult ?result .
      OPTIONAL {
        ?observation sosa:observedProperty <property/HDOP> ;
                     sosa:hasSimpleResult ?hdopValue .
      }
      FILTER (!BOUND(?hdopValue))
    }
      
      ```
  - **Result:** No output (query returned no results)
### 6. Juling's GPS Readings
- What readings have been recorded by Juling when the sensor type contains GPS?
  - **Generated SPARQL Query:**
    ```sparql
    PREFIX sosa: <http://www.w3.org/ns/sosa/>
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX : <http://api.stardog.com/>
    
    SELECT ?reading ?property
    WHERE {
      ?observation sosa:madeBySensor <python/Juling> ;
                   sosa:observedProperty ?propertyUri ;
                   sosa:hasSimpleResult ?reading .
      ?propertyUri rdfs:label ?property .
      FILTER CONTAINS(STR(?property), "GPS")
    }
      
      ```
  - **Result:** No output (query returned no results)
### 7. Liun's Directional Data
- Show me the Liun readings from when its direction was towards the north.
  - **Generated SPARQL Query:**
    ```sparql
    PREFIX sosa: <http://www.w3.org/ns/sosa/>
    PREFIX : <http://api.stardog.com/>
    
    SELECT ?reading ?value
    WHERE {
      ?directionObservation sosa:madeBySensor <elephant/Liun> ;
                            sosa:observedProperty <property/direction> ;
                            sosa:hasSimpleResult "North" ;
                            sosa:resultTime ?time .
      
      ?reading sosa:madeBySensor <elephant/Liun> ;
               sosa:resultTime ?time ;
               sosa:hasSimpleResult ?value .
    }
      
      ```
  - **Result:** No output (query returned no results)
### 8. Kuma's Altitude Query
- Are there any readings from Kuma with an altitude greater than 1000 meters?
  - **Generated SPARQL Query:**
    ```sparql
    PREFIX sosa: <http://www.w3.org/ns/sosa/>
    PREFIX geo: <http://www.w3.org/2003/01/geo/wgs84_pos#>
    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
    
    ASK
    WHERE {
      ?observation sosa:madeBySensor <elephant/Kuma> ;
                   sosa:observedProperty geo:alt ;
                   sosa:hasSimpleResult ?altitude .
      FILTER(xsd:float(?altitude) > 1000)
    }
      
      ```
  - **Result:** No output (query returned no results)
### 9. Kasih's Time-Bound Data
- Are there any readings from Kasih with a result time between January 5, 2022, and January 6, 2022?
  - **Generated SPARQL Query:**
    ```sparql
    PREFIX sosa: <http://www.w3.org/ns/sosa/>
    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
    
    ASK {
      ?observation sosa:madeBySensor <elephant/Kasih> ;
                   sosa:resultTime ?time .
      FILTER (?time >= "2022-01-05T00:00:00"^^xsd:dateTime && ?time <= "2022-01-06T23:59:59"^^xsd:dateTime)
    }
      
      ```
  - **Result:** No output (query returned no results)
### 10. Juling's HDOP Value
- When was the HDOP value <= 10 for the Juling chip?
  - **Generated SPARQL Query:**
    ```sparql
    PREFIX sosa: <http://www.w3.org/ns/sosa/>
    PREFIX : <http://api.stardog.com/>
    
    SELECT ?time
    WHERE {
      ?observation sosa:madeBySensor <python/Juling> ;
                   sosa:observedProperty <property/HDOP> ;
                   sosa:hasSimpleResult ?hdopValue ;
                   sosa:resultTime ?time .
      FILTER(?hdopValue <= 10)
    }
      
      ```
  - **Result:** No output (query returned no results)
 
    
