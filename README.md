                                                            Web-Clustering-APP
***
I have developed a web application in which you can cluster your data from a CSV file. In order for the application to recognize which coordinate column to use as X and which one to use as Y, the user must specify the names of the columns in the file that contain the coordinates to be used as the coordinates on the graph. Clustering is implemented using the K-Means method and the Silhouette coefficient. After successful clustering, the application displays a graph of the clusters, along with the name of the larger cluster and the number of points within it. Visualization is implemented using the Dash library. The app has an account system, so you can save the names of the files you've worked with in your account. Here's the source code and CSV files you can use to test the app (you can upload your own).
***
                                                                  Server:
*To implement the server side of the project, we chose Flask, a microframework for developing web applications in Python. Flask uses the Werkzeug and Jinja2 libraries, providing a minimal set of tools for creating web applications. One of the key aspects is URL routing (routing). Routing defines the relationship between user requests and server functions. Each route is mapped to a function that handles the request and returns a response. For example, when a user visits the URL '/reg', they will be redirected to the 'register.html' page. Adding the necessary routes for the pages is an important step. The server is hosted on a host.The host is Localhost, which represents a local computer that initiates a request without access to an external network. The default IP address for Localhost is 127.0.0.1. Port 8000 is selected for this host.
***
                                                                 Register:
*To save the history of clustered files, I have added an account system that works as follows:The user enters a login, password, and email address in the form. The system verifies the entered data by matching it with the information stored in the JSON database. If there is no match, the system generates a unique identifier (ID) for the new user and stores the provided data in an array. To enhance security, the password is hashed using the hashlib library before being stored in the database. This module provides a wide range of cryptographic hash functions, including MD5, SHA-1, and SHA-256. For example, the password "12345" is converted to the hash value "4cb9ff00fb76771399a70b1656947a10633a7763488925fbb6804b7ea94240d4". After successful registration, the user can authenticate in the system. 
***
                                                                 Log-in:
*After successful registration in the system, the user is provided with the option to log in. The login process involves entering the credentials in the corresponding form, after which the entered password is hashed. The generated hash is compared with a JSON array containing information about the accounts. If the entered login and hashed password match the data in the array, the authentication function returns a Boolean value of True, indicating successful login. Once the user is successfully authenticated, they are redirected to the clustering page. Given the application's routing structure, there is a risk of unauthorized access to any page by directly specifying the route name. To address this vulnerability, a user session management mechanism has been implemented. After successful authentication, a user object is created, which contains all the necessary information about the current user. Whenever a route is attempted to be navigated, the system checks for the existence of the created
***
                                                           Silhouette coefficient:
*The silhouette coefficient is a method of interpreting and checking the consistency within data clusters. This method allows you to visually show how well each object is classified. It is a measure of how similar an object is to its own cluster (connectivity) compared to other clusters (separation). The silhouette value ranges from -1 to +1, where a high value indicates that the object fits well with its own cluster and does not fit well with neighboring clusters. If most of the objects have a high value, then the clustering configuration is suitable. If many points have a low or negative value, there may be too many or too few clusters in the clustering configuration. Clustering with an average silhouette width of more than 0.7 is considered "strong," more than 0.5 is considered "reasonable," and more than 0.25 is considered "weak," but it becomes more difficult to achieve such high values as the data dimension increases due to the curse of dimensionality, as distances with
***
                                                                 K-Means:
*In my clustering code, I used the K-Means algorithm because, comparing it with another one, it turned out to be the fastest and best. The algorithm is an iterative procedure: The number of clusters k is selected using the silhouette coefficient. From the initial set of data, k observations are randomly selected to serve as the initial cluster centers. For each observation of the initial set, the nearest cluster center is determined, the distances are measured in the Euclidean metric: (d = √[(x2 - x1)2 + (y2 - y1)2]). In this case, the records "pulled" by a certain center form the initial clusters. The centroids - the centers of gravity of the clusters are calculated. Each centroid is a vector whose elements are the average values of the corresponding features calculated over all records of the cluster. The center of the cluster is shifted to its centroid, after which the centroid becomes the center of the new cluster. Then the steps are repeated iteratively.
***
                                                                 Dash:
*Dash is a framework built on top of Flask and React that allows you to create web applications in Python. With Dash, you can easily integrate graphs from Plotly into web pages and add interactive elements such as buttons, drop-down lists, and sliders.                     
***

                                                         Clusterization history:
*After the graph is displayed on the screen, the user can save the name of the clustered file to the library. When the user attempts to save the file, a database validation function is triggered. If the user has not saved a file with the same name, the program will store the name of the file in a JSON array with the same ID as the user. If the user has already saved a file with the same name, the addition will be denied.
***
                                              Information about project files:
***
1) Programming language: Python 3.13
2) Markup and styling languages: HTML, CSS
3) Framework for creating a server: 'Flask'
4) Startup file: 'main_server.py'
5) Clusterization file: 'clusterization.py'
6) Visualization file: 'visual.py'
7) Data transfer files in the app: 'test.csv', 'test-user.csv'
8) File with data path: 'data_path.py'
9) Login file: 'login_process.py'
10) Registration file: 'registration_process.py'
11) File for converting arrays to json and json to arrays: 'utils.py'
12) File to check for saved files: check_files.
13) User data files: directory 'Data' ('data.json', 'cluster-save.json')
14) HTML files: directory 'Templates'
15) The language of the error system in the terminal: Russian
***
 Libraries and tools used in creation: 
***
  1) black==25.1.0
  2) flasher==1.9.0
  3) certificate ==2025.1.31
  4) kffi==1.17.1
  5) encoding-normalizer==3.4.1
  6) click==8.1.8
  7) cluster==1.4.1.post3
  8) colorama==0.4.6
  9) contourpy==1.3.1
  10) cryptography==44.0.2
  11) cycler==0.12.1
  12) dash==2.18.2
  13) dash-core-components==2.0.0
  14) dash-html-components==2.0.0
  15) dash-table==5.0.0
  16) Flask==3.0.3
  17) fonttools==4.56.0
  18) gcloud==0.18.3
  19) gitdb==4.0.12
  20) GitPython==3.1.44
  21) googleapis-common-protos==1.69.1
  22) httplib2==0.22.0
  23) idna==3.10
  24) importlib_metadata==8.6.1
  25) this is dangerous==2.2.0
  26) Jinja2==3.1.6
  27) joblib==1.4.2
  28) jwcrypto==1.5.6
  29) jwt==1.3.1
  30) kiwisolver==1.4.8
  31) MarkupSafe==3.0.2
  32) matplotlib==3.10.1
  33) mypy-extensions==1.0.0
  34) narwhals==1.30.0
  35) nest-asyncio==1.6.0
  36) numpy==2.2.3
  37) oauth2client==4.1.3
  38) packaging==24.2
  39) pandas==2.2.3
  40) path description==0.12.1
  41) cushion ==11.1.0
  42) platforms==4.3.6
  43) plot==6.0.0
  44) protobuf==5.29.3
  45) pyasn1==0.6.1
  46) pyasn1_modules==0.4.1
  47) pycparser==2.22
  48) pycryptodome==3.21.0
  49) parsing==3.2.1
***      
                                                     Resources:
***
*It took me: 4 months (20 hours per week)
***
*Sources: 
1) https://ru.wikipedia.org
2) https://habr.com
3) https://qna.habr.com
4) https://www.geeksforgeeks.org
5) https://sky.pro/media
6) https://www.kaggle.com
7) https://github.com
8) https://otvet.mail.ru
9) https://pythonguides.com
10) https://stackoverflow.com
11) https://www.cyberforum.ru
12) https://www.jetbrains.com
