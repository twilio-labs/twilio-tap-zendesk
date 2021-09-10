# Changelog

## 1.0.7
    * Adding key as agent_id for agents_activity 
    * Adding help center article stream
    
## 1.0.6
    * Adding schema type "string" to call status field for agents_activity
    
## 1.0.5
   * Added stream agents_activity
   * upgraded zenpy version to 2.0.24 

## 1.0.4
    * Added optional parameter for config `end_date`
    * Added a check for end_date during data fetch from API
    * If passed, data would be loaded for `date >= start_date and date < end_date`

## 1.0.3
    * Load was failing for objects which were not present in sideload_objects list as keyerror
    * Added a check to verify if object exists in sideload list

## 1.0.2    
    * Added a new field "sideload-objects" that can be passed in the metadata of the catalog file as a list
    * A variable "SIDELOAD_OBJECTS" added which has a list of all objects that can be side loaded to tickets
    * Method added to add the schema for these side loaded objects to stream.schema which will check if these objects are valid side load objects and add the schema if true
    * Change added to fetch tickets call to include sideload objects

    
## 1.0.1
  * Add `default` and `description` fields to groups stream schema
  * Add new stream ticket_metric_events
  * Update singer-python dependency from `singer-python==5.2.1` to pipelinewise's version `pipelinewise-singer-python==1.2.0`
  * Add new fields to users stream schema
  * Add new fields to tickets stream schema
 
## 1.0.0
  * This is a fork of https://github.com/singer-io/tap-zendesk v1.5.3.
  

