                                    

################################################################################################################                           
                                    BOOKSTORE API
################################################################################################################

 Bookstore is a little backend API based on DJANGO REST FRAMEWORK and related technologies. It offers basic storing features.
 Not only it's connected to AWS RDS where it stores data, it's also connected to a AWS Bucket where it stores images.
 

                                   AUTHENTICATION TECHNOLOGY USED
----------------------------------------------------------------------------------------------------------------
 To ensure awesomes admin and user experiences with security, we used in this project rest_framework.authtoken.
        -> read more about it to see how it works


                                   BOOKSTORE FEATURES
----------------------------------------------------------------------------------------------------------------

    As features, it provides

        -> Book storing -- add a book, delete a book .. -- to admin
        -> User registration 
        -> User login
        -> All Admin management - such as delete user -- 
        -> Users with permissions or authorizations can get to book detail

                                    HOW TO USE BOOKSTORE
----------------------------------------------------------------------------------------------------------------

 ====================>  FIRST : Environment
        -> Make sure you create the requirement environment :
           - Create an environment named 'bookenv' with virtualenv and install all requirements.txt
           - Pull bookstore github repo
           - run the server with manage.py runserver command
           - get the localhost link and browse it -- recommend to use postman --
           
 ====================>  API's ENDPOINTS
        
          'obtain_token/'      ---> authenticate -- get token --
          'register/'          ---> register --as a new user --             
          'api/books/'         ---> books listing
          'api/books/<pk>/'    ---> book detail
          'api/users/'         ---> users listing -- for admins --
          'api/users/<pk>/'    ---> user detail -- for admins --
          'api/management/'    ---> books management -- add, delete enable disable --
          'admin/'             ---> adimin site
   
 THANKS FOR READING  
