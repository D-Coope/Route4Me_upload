Program to automatically create a map in Route4Me

Takes 2 inputs, a batch name and a list of postcodes

From the batch name it takes the second to last number and adds the correct outbase as the depot for the route

The user input would be redundant if incorporated into the transport system as the name of the map would be the holding batch

An API key would need setting for each user which is found in the user settings

Unable to create a map working with the R4M API without obtaining the coordinates,**line 58** in the route4me_upload file fixes that issue.
