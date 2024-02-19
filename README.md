BEHAVIOUR OF EACH FUNCTION

  get_tanks(): Returns a list of 0 or more objects. If a POST request was successfully made to the /tank route previously, the GET route should return an array of the posted tank objects.
  
  get_tank_id(): Returns a single tank that is associated with the id passed as input in the route. If the API is unable to located the object that has the id specified, the API responds with an appropriate response message and status code.
  
  add_tank(): Accepts a JSON object. On success, the web application responds with the the same JSON object that was posted with the addition of an `id` attribute. This `id` is generated by the API. The route should also returns a status code that indicates that an object was **successfully created**.
  
  alter_tanks(): Allows a client to alter the parts of one of the tanks after it has been posted. It allows the requester to make a JSON body with any combination of the three attributes and update them as necessary (The client is NOT allowed to edit the `id` attribute). The route also returns a status code that indicates that an object was **successfully altered**. If the API is unable to locate the  object that has the id specified, the API responds with an appropriate response message and status code.
  
  delete_tank(): Allows the client to delete any previously posted object. Returns a status code that indicates **success**. If the API is unable to locate the object that has the id specified, the API responds with an appropriate response message and status code.
  

REASON FOR WRITING CODE

  This code was written for the ECSE3038 Lab #3.
  

TWO TRUTHS AND A LIE
  1. I can play the piano.
  2. I have been to the top of Blue Mountain.
  3. I have been to three countries outside of Jamaica.
