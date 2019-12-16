# Google-Cloud-FileUpload
 
In this workshop you will learn how to build a file transfer web application similar to wetransfer.

## Resource to use:

- IDE
- vuejs/or reactjs - nuxt/vuejs will be supported for this workshop but you are free to use reactjs to build the application. You can even use a basic html site.
- Github account


Steps:

- Setup your Nuxtjs project and create a simple web page in html that can submit a file to the API endpoint provided in the workshop
- Once you have uploaded the file you can create additional actions such as sending email notifications to the user.

The basic API endpoint workflow:
- Submit specific information to the api endpoint to generate a signed URL
- With the returned SignedURL post the files to upload the files to Google Cloud.
- Using the uuid generate a link to view the files to download


Please note this workshop will run the api endpoints during the workshop as the package is not a fully secured solution. 
