# draup_django

[![Downloads](https://pepy.tech/badge/draup-django)](https://pepy.tech/project/draup-django)

### Delete, Update functionality for normalised models


## Use-Case : 

  * `Draup Django` provide 
  delete, update functionality for ORM(object relational mapping)level.
  
## Table of Content :
  
  * [Stateful Delete/Update](#stateful)
     * [Get Affected Objects](#get-affected-objects)
     * [Delete Object](#delete-object)
     * [Update Object](#update-object)
  * [Installation](#installation)


## Stateful Delete/Update
  * Below are functions inorder to get the stateful delete/update
 
  ### Get Affected Objects
   * List out all dependent objects(Prompt-Messages).
   * `getAffectedObjects` takes input dict with id as key and reference of model.
   
   ```
   Sample Input : ({'id':1},model_reference)
   Output : Error_list(list),prompt messages(list)
   ```
   
  ### Delete Object
   * Delete object with all the dependent objects. 
   * `deleteObject` takes input dict with id and force_delete as key and reference of model.
   
   ```
   Sample Input : ({'id':1,'force_delete':True},model_reference)
   Output : Error_list(list)
   ```
   
  ### Update Object 
   * Transferring Object dependencies from one object to another object.
   * `updateObjectDependencies` takes input source,destination objects.
   
   ```
   Sample Input : (source,destination)
   Output : Error_list(list)
   ```

## Installation
  * Use Pip to install the module
  
    ```
    pip install draup-django
    ```
    
## Usage :
  * Sample model : 
      
          class parent(models.Model):
            name = models.CharField(max_length=100)
            
          class child(models.Model):
            parent = models.ForeignKey(parent, on_delete=models.CASCADE) 
            name = models.CharField(max_length=100)
      
  *  Parent Table :
  
     | id     | Name      |
     | ------ | --------- |
     |  1     |  Alice    |
     |  2     |  Tom      |
  
 * Child Table :
  
     | id          | Name       |  parent_id    |
     | ----------- |  --------- |-------------- |
     |  1          |  Bob       |     1         |
     |  2          |  Jack      |     2         | 

  
  * Code :
         
         from draup_django import utility
         m = models.parent

         """
         Get Prompt Message
         """

         error_list,prompt_message = utility.getAffectedObjects({'id':1},m)

         """
         Deletion with all dependent objects
         """
         error_list = utility.deleteObject({'id':1,'force_delete':True},m)

         """
         Transferring Object dependencies
         """

         source = m.objects.filter(id=1).first()
         destination = m.objects.filter(id=2).first()
         error_list = utility.updateObjectDependencies(source,destination)
         
  * Output :
        Prompt Message of `getAffectedObjects` function
        
        [{'message': 'This object has been used in child 1 times.', 'model_name': 'child', 'Parent models': '', 'count': 1}] 
         
  * **Note** : 
       -  Every function returns the error_list, and hence only the operation is successful only if it is empty. 
       -  According to above Child/Parent Table `updateObjectDependencies` function will transafer object dependency from `id:1` to `id:2` so parent_id of `Bob` will become `2`. 
  
       - Updated Child Table: 
       
         | id          | Name       |  parent_id    |
         | ----------- |  --------- |-------------- |
         |  1          |  Bob       |     2         |
         |  2          |  Jack      |     2         |
   
## Limitation :
   * `updateObjectDependencies` will not work in case of unique constraint,one to one field in model.
   * Please feel free to share your thoughts and feedback at info@draup.com .
  

## About Draup :
   
  [Draup](https://draup.com) is an enterprise decision-making platform for global CXO leaders in sales and talent domains. Draup combines Artificial Intelligence with human curation to help organizations make data-driven strategic decisions. The platform is powered by machine- generated models, which are augmented by a team of analysts adding their learning-based insights to provide a 360-degree transactable view of their sales and talent ecosystem. We work on cutting edge technolgies and run highly complex algorithms on huge volumes of data. We are open sourcing certain internal tools which are not part of our core propietary business algorithms.
   
