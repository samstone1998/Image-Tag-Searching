# Image-tag-searching
A Django webapp that has a Giphy like feature where a user can search images based on the text and content inside the image. After finding out that Google has a Vision api that is public I wanted to implement it into one of my own webapps.

The actual image tag indexing is done using celery tasks as I have noticed this can take up to 45 seconds to get all the tags for the image. Doing this in the background rather then having the user wait gives a much better experience.

I know the front end design is not the nicest but the idea of this webapp is the features/processes it entails rather then the front end design.

### How it works
When the user uploads an image a background celery task is then started that runs this image through Googles vision api. All the text and content 'tags' that the api returns are then stored into a database against that image. I then used Postgres search functionality to allow users to search based on these tags.

I have found however that sometimes Googles Vision api misses certain content or uses acronyms that a normal user would not search for.

## How to run
Before being able to run you need to set up Google vision api and get a json config to authenticate. To do this I recommend you follow this guide
```
https://cloud.google.com/vision/docs/setup
```
Once set up save your config in the main folder (where this README is) as **django-image-search-config.json**. We are now ready to get the docker file running.

Install Docker for you system using the link below.
```
https://docs.docker.com/get-docker/
```

With Docker installed and running open a terminal in the main folder and run the command below
```
docker-compose build  
```

Once build we then need to bring the containers up
```
docker-compose up -d --build
```

Now wait around 15-20 seconds so that Django can do the database migrations and so all services have time to completly start up. You should then have a working Docker enviroment.

Go to localhost on port 8000 and you should see a home page. From here upload an image and try search for features inside that image to see if the image appears. 

Please note sometimes it can take 30 seconds or so for the image to actually appear in searches. This is because the background task needs to index the tags for that image. On very rare ocasions I have seen this take up to 45 seconds.





## Useful resources
https://cloud.google.com/vision/docs/setup