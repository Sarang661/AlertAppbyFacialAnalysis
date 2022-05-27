# AlertAppbyFacialAnalysis
 A countless number of people drive on the highway day and night. Taxi drivers, bus drivers, truck drivers and people traveling long-distance suffer from lack of sleep. People traveling long-distance suffer from lack of sleep. Due to which it becomes very dangerous to drive when feeling sleepy or angry or sad. So, to prevent these accidents I have build a web application using Python, Django which will alert the driver when he feels angry or sad or surprised.







## Tech Stack

**Client:** HTML, CSS, JavaScript

**Server:** Django, Python

**Database:**  SQLite3 for local machine, Postgresql for deployment

**Other:** OpenCV, Image Processing, Machine learning, Face recognition



 ## Architecture


![5_DjangoApp pptx  Protected View  - PowerPoint 27-05-2022 22_00_51](https://user-images.githubusercontent.com/85448041/170760181-94da08a8-7c94-4f9e-bd93-1e686abdc0a0.png)

 


## OpenFace Feature Extraction Method

 ![4_Feature_Extraction_from_face pptx  Protected View  - PowerPoint 27-05-2022 23_06_45](https://user-images.githubusercontent.com/85448041/170763087-c0e300dd-31ad-490f-9b8d-8e3e0b472350.png)


## Run Locally

Clone the project

```bash
  git clone https://github.com/Sarang661/AlertAppbyFacialAnalysis.git
```


Install dependencies

```bash
  pip install virtualenv

  virtualenv myenv

  myenv\Scripts\activate

  pip install -r requirements.txt

```

Start the server

```bash
  python manage.py runserver
```


## Project Demo
<br />

### 1) Go to https://alertappbyfacialanalysis.herokuapp.com/

<br />
<br />

![Driver Alert App - Google Chrome 27-05-2022 23_32_09](https://user-images.githubusercontent.com/85448041/170768460-9ed9801a-71c7-4fbc-9934-6cb7ef60a0b7.png)

<br />
<br />

### 2) Choose the image for processing

<br />
<br />



![Driver Alert App - Google Chrome 27-05-2022 23_33_00](https://user-images.githubusercontent.com/85448041/170768743-7e0c33d6-b314-42fb-a972-9ddf6b5fc0e7.png)
<br />
<br />
### 3) You will get Alert based on the emotion detected in image and face analysis of face detected in iamge. Multiple faces can be detected in the image.

<br />
<br />



![Driver Alert App - Google Chrome 27-05-2022 23_34_08](https://user-images.githubusercontent.com/85448041/170769720-1a92b77c-b1bb-4195-9353-997b5e569918.png)

![Driver Alert App - Google Chrome 27-05-2022 23_44_02](https://user-images.githubusercontent.com/85448041/170769751-ca0fceba-dcf7-4bce-8de9-cc1e34e8d1a0.png)
