# **The Fitness Kitchen** 

As part of my Milestone 3 project with [Code Institute]( https://codeinstitute.net/) i was challenged with designing, developing and implementing a back-end for a web application using Python and the
[flask micro-framework]( https://flask.palletsprojects.com/en/1.1.x/), allowing users to create, read, update and delete(CRUD) data entries on a fully responsive full stack web application. 

I have decided to create an online healthy cooking recipe website which promotes healthy meals. All the recipes are healthy nutritious meals, which are also tasty and eye catching proving to the user that eating healthy doesn’t have to be mundane. 
Each recipe includes everyday ingredients you can find in your local supermarket, and have easy to follow preparation and cooking methods that accommodates people of all cooking skill levels. 
Users are able to add, delete and update their own recipes so the website can be a one stop shop for all their healthy recipes. 

[view the live project here.](https://milestone-3-pcn.herokuapp.com/)

<h2 align="center"><img src="README/images/milestone3-responsive.png" max-width="50%"></h2>

## **USER EXPERIENCE (UX)**
The idea of a recipe website isn't something new, but this website is moving the goal post's by making <strong>'The Healthy Kitchen'</strong> a one stop shop for all your healthy recipes. Everyone has endless access to different recipe's, from influencers to tv chefs, and  from websites or social media pages to the old fashioned recipe book. One problem users face, is they have to trawl through all these mediums to find their recipe. The <strong>'The Healthy Kitchen'</strong> is the solution. Registered Users can add, edit and delete their own recipes and have access to all the other recipes uploaded to the website. Un-registered users also have access to the recipes on the website the main difference being they don't have access to the CRUD functionality.

Users can filter the recipes to select meals from the following categories: /breakfast meals/lunch/dinner/vegetarian category/Gluten Free. 


-   ### **USER STORIES** 
  
 1. As a user I want to see healthy nutritious meals that encourage me to cook and eat healthy.
     - When the user comes to the main page of the site they are greeted with all the various recipes and a brief supporting summary of each meal.

  2. As a user I want the recipes to be broken into categories so I can filter the recipes shown to me.  
     - Reason for filtering option where user can select between breakfast, lunch or dinner food recipes and also a vegetarian filter. 
    
3. As a user I want to get more detailed look once I click on the recipe.
    - Supporting html page for each recipe with detailed information for the meal and the method of preparation.  

4. As a user I want to be able to add my own recipes so I can use this website as a one stop shop for all my recipes. 
    - Reason for ‘Add Your Own Recipe Page’. 

5. As a user I want to be able to delete or update/edit the recipes I added to the website.
    - Reason for users being able to edit/delete their recipes.

6. As a user I want to easily understand the purpose of the site and learn what the owner’s beliefs are.
   - Reason for about page. 

7. As a site owner, I want to ensure my website is secure, and I want to keep a dataset of my users.
    - Reason for login/registration. 


-   ### **WIREFRAMES**

After reading the project brief i formulated a idea and jotted down notes and rough sketches on pen and paper. These ideas evolved into creating user stories which helped me formulate a plan to draw up some wireframes.
I used [Balsamic](https://balsamiq.com/) to build the wireframes. I created mockups for desktop, tablet and mobile viewports, so i could have an idea of what my website would look like, and i could follow a plan to avoid scope creep.

<details>
<summary>Desktop Wireframes <strong>(Click dropdown for images)</strong></summary>
<p align="center">
  <img height="350" src="wireframes/images/hero_wireframe.png" style="max-width:100%;"></a>
</p>
<p align="center">
  <img height="350" src="wireframes/images/recipe_wireframe.png" style="max-width:100%;"></a>
</p>
<p align="center">
  <img height="350" src="wireframes/images/recipe_selected_wireframe.png" style="max-width:100%;"></a>
</p>
<p align="center">
  <img height="350" src="wireframes/images/add_edit_wireframe.png" style="max-width:100%;"></a>
</p>
<p align="center">
  <img height="350" src="wireframes/images/about_wireframes.png" style="max-width:100%;"></a>
</p>
<p align="center">
  <img height="350" src="wireframes/images/login_register_wireframe.png" style="max-width:100%;"></a>
</p>
</details>

<details>
<summary>Tablet Wireframes <strong>(Click dropdown for images)</strong></summary>
<p align="center">
  <img height="350" src="wireframes/images/ipad_wireframe.png" style="max-width:100%;"></a>
</p>
</details>

<details>
<summary>Mobile Wireframes <strong>(Click dropdown for images)</strong></summary>
<p align="center">
  <img height="350" src="wireframes/images/mobile_wireframes.png" style="max-width:100%;"></a>
</p>
</details>

## **Design**

### Framework
I used [Bootstrap 4]( https://getbootstrap.com/) to build the framework of the website. Bootstrap was  the main tool frame responsible for making the PCN website responsive. This means the website automatically resizes itself to look good on all devices, be it mobile, tablet, laptop or desktop. 

### Colour Scheme

- **Black** - Black is the dominant colour throughout this website. Black is elegant, sophisticated and it implies a premium brand. The black background gives prominence the content on the site.

- **Burnt Orange** - (#BF5D1D) This Burnt Orange colour is consistently used throughout the website call to action buttons, flash messages and other subtle styling. This shade of orange is juxtaposed well with the elegant black to offer a modern feel which fits well within the health industry.

- **Silver** - (#B7B4B2) This Silver colour is the main font colour for the body of the website. It is also used in the borders of the entry forms to offer a 3d feel against the black background.

- **Gold** - (#BC9982) This Light shade of gold is used predominantly for the headings of the website. The light cold contrast well with the background and with the Oswald font gives a classy feel.

#### List of the other colours used throughout the website: 
 
-  #111111 (Lighter Shade of Black)

- #46B123ED (Green)

- #DC3545 (Red)

- Whitesmoke

- White

### Typography 
The “Oswald” font is the font used for all the headings and the “Open Sans” font is the font used for the body of the website. Sans serif is set as the fallback font in case for any reason the font isn't being imported into the site correctly.

### Imagery
Imagery is a reoccurring theme throughout the website. I felt images played a vital role in influencing a users decision in choosing a recipe. 
The Hero image especially works well in drawing the user in and given the website a very modern feel.

### Logo
I created the logo on [Tailor Brands]( https://www.tailorbrands.com/). Although it is a paid service i feel the level of detail and quality of the template they use is worth it. I decided to go with a logo with a slogan for personal reasons as i have used mostly initial styled logos in the past. The slogan here "Eat Yourself Healthy" acts like a call to action, enticing the user to navigate the website and hopefully register an account. The Red logo color and the black font works well against the clean hero image. 
<h2 align="center"><img src="README/images/logo_readme.jpg" max-width="30%"></h2>

## **LAYOUT**

### Homepage 

The homepage sets up to be enticing while at the same time obvious to the user the purpose of the website. The Hero Image paired with the Logo sets the theme of the website as healthy food recipe site. 

- There is two obvious call to actions:

  1.   Flash Message - Informs users that they must register an account to add their own recipes. 

  2.   Recipes Button - Users are prompted to click 'Recipes' button to bring them to the main recipes page. 

<details>
<summary>Homepage <strong>(Click dropdown for images)</strong></summary>
<p align="center">
  <img height="350" src="README/images/homepage_cta.jpg" style="max-width:100%;"></a>
</p>
</details>  

---
### Recipes Page 

Although this is not the homepage of the site, it is the main page of the website. Each website is presented in the form of a [Bootstrap card]( https://getbootstrap.com/docs/4.0/components/card/#card-groups). Users get a snippet of the recipe, and can get more details of each recipe if they click the button on the button of each recipe card deck. 
Users can also use the filtered dropdown to select different recipe categories(breakfast/lunch/dinner/vegetarian/Gluten Free). 
I included a pagination feature on this page, to safeguard against the future growth of this website where users would potentially have to scroll endlessly whilst browsing the website. 
With the pagination function, the recipe's page is capped at 9 recipes per page.

Users do not need to be logged in to access this page. 

<details>
<summary>Card Deck <strong>(Click dropdown for images)</strong></summary>
<p align="center">
  <img height="350" src="README/images/card_deck.png" style="max-width:100%;"></a>
</p>
</details>  
<details>
<summary>Filter Dropdown <strong>(Click dropdown for images)</strong></summary>
<p align="center">
  <img height="350" src="README/images/dropdown.png" style="max-width:100%;"></a>
</p>
</details>  
<details>
<summary>Pagination <strong>(Click dropdown for images)</strong></summary>
<p align="center">
  <img height="350" src="README/images/pagination.jpg" style="max-width:100%;"></a>
</p>
</details>  

---
### About Page 
The About page is to reaffirm to the user the purpose of the website. The user will be able to gain trust that **'The Fitness Kitchen'** is a genuine brand and set up for genuine reasons. 

Login is not required for this page as this may be the final affirmation the user needs before register an account with **'The Fitness Kitchen'**

<details>
<summary>About Page <strong>(Click dropdown for images)</strong></summary>
<p align="center">
  <img height="350" src="" style="max-width:100%;"></a>
</p>
</details>  

---

### Recipe Selected Page 
Once the user clicks the recipe button on the card deck they are brought to that specific recipes details, ingredients and method. 
Users are not required to log in to access these pages. If the user is logged in and they are the author of that specific recipe they have access to edit and delete the recipe. 

<details>
<summary>Default View (no edit/delete) <strong>(Click dropdown for images)</strong></summary>
<p align="center">
  <img height="350" src="README/images/recipe_default.png" style="max-width:100%;"></a>
</p>
</details>  
<details>
<summary>Edit and Delete Buttons appear if the user is logged in and they've created the recipe <strong>(Click dropdown for images)</strong></summary>
<p align="center">
  <img height="350" src="README/images/users_recipe.jpg" style="max-width:100%;"></a>
</p>
</details>  

---
### Add Recipe / Edit Recipe 

The Add and Edit recipe pages are very similar. The only main difference is that the fields are pre-populated with the fields the user inputted when they initially added the recipe. All fields are required so the user can't leave any blank recipes. 

Login is required for these pages. 
<details>
<summary>Add Recipe <strong>(Click dropdown for images)</strong></summary>
<p align="center">
  <img height="350" src="README/images/add_recipe.png" style="max-width:100%;"></a>
</p>
</details>  
<details>
<summary>Edit Recipe <strong>(Click dropdown for images)</strong></summary>
<p align="center">
  <img height="350" src="README/images/.png" style="max-width:100%;"></a>
</p>
</details>  

---
### Delete Recipe 
The Delete Recipe functionality doesn't have a page on its own, but if the user is logged in and they wish to delete their recipe, they are presented with a model to confirm deletion. This is to safeguard against a user deleting a recipe unintentionally. 

Users must be logged in, and they must be the creator of that specific recipe in order to have access to delete the recipe. 

<details>
<summary> Delete Recipe <strong>(Click dropdown for images)</strong></summary>
<p align="center">
  <img height="350" src="README/images/delete_recipe.png" style="max-width:100%;"></a>
</p>
</details>  

---
### My Recipes
If Users are logged in , they can click the 'My Recipe' tab on the nav bar and it will showcase only the recipes the user has added. 
Pagination is also included on this page for the very reasons outline in the Recipes Page. 

<details>
<summary> My recipes <strong>(Click dropdown for images)</strong></summary>
<p align="center">
  <img height="350" src="README/images/my_recipes.png" style="max-width:100%;"></a>
</p>
</details>  

---
### Login and Registration Pages
Authentication wasn't required for this Milestone Project, but after I implemented the CRUD functionality and I had a minimum viable product, i decided to implement a login and registration. Having authentication allows for a more secure website. Users can't delete other user's recipes. Authentication also allows the website to be more personal. Users have their own 'My Recipes section' and are also greeted with their session username in the flash messages. 

If users are already logged in and unintentionally get redirected to the 'Login' page by the browser, they will be redirected to their own recipes page and a flash message will greet them "You are already logged in". I decided against redirecting logged in users away from the 'Register' page as it's not a distinct possibility that a user may want to register another account. 

<details>
<summary>Login Page <strong>(Click dropdown for images)</strong></summary>
<p align="center">
  <img height="350" src="README/images/login.png" style="max-width:100%;"></a>
</p>
</details>  

<details>
<summary>Register Page <strong>(Click dropdown for images)</strong></summary>
<p align="center">
  <img height="350" src="README/images/register_page.png" style="max-width:100%;"></a>
</p>
</details>

<details>
<summary>Enter (/login) in the browser and Already Logged, redirected with message <strong>(Click dropdown for images)</strong></summary>
<p align="center">
  <img height="350" src="README/images/user_already_logged_in.jpg" style="max-width:100%;"></a>
</p>
</details>  

<details>
<summary>Personal greeting upon Logging in<strong>(Click dropdown for images)</strong></summary>
<p align="center">
  <img height="350" src="README/images/log_in_message.jpg" style="max-width:100%;"></a>
</p>
</details>  

---
### Access Denied Page 
if a user is not logged in and tries intentionally or unintentionally to reach a page that requires a session log in, then they will be greeted with this message below. 
Users have the option to log in, register or else navigate back by clicking the previous button on the browser tab. 

<details>
<summary>Access Denied<strong>(Click dropdown for images)</strong></summary>
<p align="center">
  <img height="350" src="README/images/access_denied.png" style="max-width:100%;"></a>
</p>
</details>  

---
### Base Template 
The base.html contains the basic layout which is common to all the other templates, and it is from this base template that we extend the layout for other pages.
We modify the parent template(base.html) using the child templates (e.g the pages listed above). The {% extend %} must be the first tag in the child templates. This tag tells the template engine that this template extends from the parent template or ( base.html ).

We then use Template inheritance eg. 

    {% block content %}
    {& endblock %}

To override the base.html page and add our custom code to the child elements. 

The Base.Html page in this website contains all the relevant links to our bootstrap framework, font awesome, css files, Jquery and other relevant meta tags. The Base.html also sets the template for the navbar and flash messages used throughout the website and the reoccurring css styles like font, colour, background colour etc. 

The Navbar differs slightly for users who are logged in and users who are not. 

Users who are logged in see 'Recipes / About / Login / Register". 

Users who are not logged in see "Recipes/ Add Recipes / My Recipes / Logout".

<details>
<summary>Navbar for logged in users <strong>(Click dropdown for images)</strong></summary>
<p align="center">
  <img height="350" src="README/images/navbar_logged_in.jpg" style="max-width:100%;"></a>
</p>
</details>  

<details>
<summary>Navbar for user's who are not logged in <strong>(Click dropdown for images)</strong></summary>
<p align="center">
  <img height="350" src="README/images/navbar_not_logged_in.jpg" style="max-width:100%;"></a>
</p>
</details>  

---

## TECHNOLOGIES

### Languages Used 

1.  [HTML5]( https://en.wikipedia.org/wiki/HTML5) - is the standard markup language for documents designed to be displayed in a web browser.
2. [CSS3]( https://en.wikipedia.org/wiki/Cascading_Style_Sheets) - Cascading Style Sheets is a style sheet language used for describing the presentation of a document written in a markup language like HTML.
3. [Python]( https://www.python.org/) - Python is an interpreted, high-level, general-purpose programming language.
4. [Javascript/Jquery]( https://en.wikipedia.org/wiki/JavaScript) - JavaScript is among the most powerful and flexible programming languages of the web. It powers the dynamic behavior on most websites.**

 ** JavaScript wasn't used directly in this project but it was imported by Bootstrap for some of the functionality(eg. Collapsible Navbar, Model)

 ### Frameworks, Libraries & Programs Used 


 1. [Bootstrap 4.4.1:]( https://getbootstrap.com/docs/4.4/getting-started/introduction/)
    - Bootstrap was used to assist with the responsiveness and styling of the website.</li>

 2. [Flask]( https://flask.palletsprojects.com/en/1.1.x/)
    - Flask is a lightweight WSGI web application framework. It is designed to make getting started quick and easy, with the ability to scale up to complex applications.

3. [Google Fonts:]( https://fonts.google.com/)
    - Google fonts were used to import the 'Oswald' font and the 'Open Sans' font into the style.css file which is used on all pages throughout the website.

4. [Font Awesome:]( https://fontawesome.com/)
    - Font Awesome was used on throughout the website to add icons for aesthetic and UX purposes.

5.  [Git]( https://git-scm.com/)
    - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.

6. [GitHub:]( https://github.com/)
    - GitHub is used to store the projects code after being pushed from Git.

7. [Balsamiq:]( https://balsamiq.com/)
    - Balsamiq was used to create the wireframes during the design process.

8. [PEP8]( http://pep8online.com/)
    - Python style guide checker. PEP8 is a tool to check your Python code against some of the style conventions in PEP 8.

9. [MongoDB]( https://www.mongodb.com/)
    - MongoDB is a cross-platform document-oriented database program. 

10. [The W3C Markup Validator]( https://validator.w3.org/) and [W3C CSS Validator Services]( https://jigsaw.w3.org/css-validator/) 
    - Used to validate the HTML and CSS of the project to ensure there were no syntax errors in the project.

## FEATURES

- CRUD functionality is the main features of the project. 
    - **Create** Logged in users can create a new recipe by submitting the add recipe form. Users who are not registered can also create an account. 
    - **Read** All users have access to see all the recipe cards and can select each recipe for more details if they are logged in or not.
    - **Update** Logged in users can edit only their own recipes. 
    - **Delete** Logged in users can delete only their own recipes. 

- Locate - Users can filter recipes under different categories in the dropdown menu. 
- Pagination - is used on the recipes page and my recipes page in order to de-clutter the website page. 


### Future Implementation

- I would look to improve the process of uploading an image to [MongoDB]( https://www.mongodb.com/) 
    - Currently users can only upload images by providing the web address. I found this [Pretty Printed]( https://www.youtube.com/watch?v=DsgAuceHha4) tutorial on Youtube which could help with this functionality, but with the tight two week time frame i didn't have time to implement this.
- Filter by date on 'Recipes' page and 'My Recipes Page'.
    - This would help so fresh content is shown first. 
- Admin Account
    - Currently i only have access to delete and change data from [MongoDB]( https://www.mongodb.com/). It would be more efficient to have permission and access to manage the website from an Admin Account.
- Users Interaction  
    - Allow users to comment on other recipes and also rate recipes. 
- Full Text Search
    - I felt this would be more appropriate for when the website grows and their is more content for the user to search through. 
- Delete an Account. 
    - Allow users access to delete their own account so they don't feel trapped by **The Fitness Kitchen**. 

## TESTING 
Manual testing was the only requirement to access the functionality, usability and responsiveness and data management of my full stack web application.
Debugging was carried out on an ongoing basis throughout of the project. Whilst coding i would preview run my code in the browser and check for any bug issues and make changes and fixes on an ad hoc basis.

I carried out manual testing and documented any errors/random side-effects captured in the DevTools. I loaded the website several times, and forced browser refresh to try and catch any errors but thankfully there was none.

<details>
    <summary>Dev Tool Testing <strong>(Click dropdown for images)</strong></summary>
    <p align="center">
    <img height="350" src="README/testing/dev_tool.jpg" style="max-width:100%;"></a>
    </p>
    </details> 

### Responsiveness
I carried out extensive testing of the responsiveness of my website by checking how the website rendered on different devices and on lower screen widths.
I have showcased screngrabs of how the website pages rendered on desktop/laptop view, tablet and mobile view. 

Testing in [Chrome Developer Tools]( https://developers.google.com/web/tools/chrome-devtools) was carried out on an ongoing basis to check the repsonsiveness and carried out debugging of issues.

#### HomePage (Hero Image)
Whilst working on the project i didn't like how the fruit and vegetables on the Hero Image went out of view on smaller screen widths below 992px so i implimented a media query to solve this issue.

<details>
    <summary>Home Page Responsiveness <strong>(Click dropdown for images)</strong></summary>
        <p align="center">
        <img height="350" src="README/testing/responsiveness_home.png" style="max-width:100%;"></a>
        </p>
        <p align="center">
        <img height="350" src="README/testing/responsiveness_home_ipad.png" style="max-width:100%;"></a>
        </p>
        <p align="center">
        <img height="350" src="README/testing/responsiveness_home_mobile.png" style="max-width:100%;"></a>
        </p>
</details> 

#### Recipes Page
During debugging i didn't like the look of how the recipes page rendered on Ipad only (not Ipad Pro) so i made a media query for tabelt screen widths with changed the image size and font size. I didn't provide screengrabs for the filtered recipes pages or the 'My Recipe's Page as they follow the same template.

<details>
    <summary>Recipe Page Responsiveness <strong>(Click dropdown for images)</strong></summary>
        <p align="center">
        <img height="350" src="README/testing/responsiveness_recipes.png" style="max-width:100%;"></a>
        </p>
        <p align="center">
        <img height="350" src="README/testing/responsiveness_recipes_ipad.png" style="max-width:100%;"></a>
        </p>
        <p align="center">
        <img height="350" src="README/testing/responsiveness_recipes_mobile.png" style="max-width:100%;"></a>
        </p>
</details> 

#### Add/Edit Recipe
I just provided the screen grab's of the add recipe form as the edit form follows the same template. The form fields are single columns on smaller screen widths. 
<details>
    <summary>Add/Edit Recipe Page Responsiveness <strong>(Click dropdown for images)</strong></summary>
        <p align="center">
        <img height="350" src="README/testing/responsiveness_add_recipe.png" style="max-width:100%;"></a>
        </p>
        <p align="center">
        <img height="350" src="README/testing/responsiveness_add_recipe_ipad.png" style="max-width:100%;"></a>
        </p>
        <p align="center">
        <img height="350" src="README/testing/responsiveness_add_recipe_mobile.png" style="max-width:100%;"></a>
        </p>
</details> 

#### Login, Registration and Access Denied Pages  
Nothing was changed for these pages as they rendered fine on all devices
<details>
    <summary>Login Page Responsiveness <strong>(Click dropdown for images)</strong></summary>
        <p align="center">
        <img height="350" src="README/testing/responsiveness_login.png" style="max-width:100%;"></a>
        </p>
        <p align="center">
        <img height="350" src="README/testing/responsiveness_login_ipad.png" style="max-width:100%;"></a>
        </p>
        <p align="center">
        <img height="350" src="README/testing/responsiveness_login_mobile.png" style="max-width:100%;"></a>
        </p>
</details> 
<details>
    <summary>Registration Page Responsiveness <strong>(Click dropdown for images)</strong></summary>
        <p align="center">
        <img height="350" src="README/testing/responsiveness_register.png" style="max-width:100%;"></a>
        </p>
        <p align="center">
        <img height="350" src="README/testing/responsiveness_register_ipad.png" style="max-width:100%;"></a>
        </p>
        <p align="center">
        <img height="350" src="README/testing/responsiveness_register_mobile.png" style="max-width:100%;"></a>
        </p>
</details> 
<details>
<summary>Access Denied Page Responsiveness <strong>(Click dropdown for images)</strong></summary>
        <p align="center">
        <img height="350" src="README/testing/responsiveness_access_denied.png" style="max-width:100%;"></a>
        </p>
        <p align="center">
        <img height="350" src="README/testing/responsiveness_access_denied_ipad.png" style="max-width:100%;"></a>
        </p>
        <p align="center">
        <img height="350" src="README/testing/responsiveness_access_denied_mobile.png" style="max-width:100%;"></a>
        </p>
</details> 


### Testing on different browsers and devices 

I created a Testing Matrix in Excel to record my findings. 

<details>
    <summary>Testing Matrix<strong>(Click dropdown for images)</strong></summary>
    <p align="center">
    <img height="350" src="README/testing_matrix/testing_matrix.png" style="max-width:100%;"></a>
    </p>
</details> 

* **the main points from this type of testing**
    
  - The Website was tested on Google Chrome,Internet Explorer, Microsoft Edge, Mozilla Firefox and Safari browsers.

  - The website was viewed on a variety of devices such as Desktop, Large Monitor, Laptop, iPhone7, iPhone 8 & iPhoneX and other samsung devices.

  - A large amount of testing was done to ensure that all pages were linking correctly.

  - Friends and family members were asked to review the site and documentation to point out any bugs and/or user experience issues.

  - Internt Explorer performed poorly yet again. Buttons are either positioned incorrectly or don’t appear at all. Horizontal rules are also out of position on Internet Explorer.         

## Testing of User Stories 

1. As a user I want to see healthy nutritious meals that encourage me to cook and eat healthy.
    * On the Recipes page the user is greeted with a page full of eye catching reicpe images encouraging the user to browse through the diffrent options. Upon clicking the recipe button under the recipe card they are interested in, they are brought to the recipe_selected page, which shows more information on that specific recipe. 
    * Each recipe contains their macronutrients so they can identify if they specific meal can fit their daily needs and be healthy. 

<details>
    <summary>User wanting healthy nutritious meals<strong>(Click dropdown for images)</strong></summary>
    <p align="center">
    <img height="350" src="README/testing/user_story_1.png" style="max-width:100%;"></a>
    </p>
    <p align="center">
    <img height="350" src="README/testing/macros.jpg" style="max-width:100%;"></a>
    </p>

</details> 

2. As a user I want the recipes to be broken into categories so I can filter the recipes shown to me.
    * On the recipes page users can click the dropdown and they can select between the different meal categories. 
    
<details>
    <summary>User Story Filter Categories<strong>(Click dropdown for images)</strong></summary>
    <p align="center">
    <img height="350" src="README/images/dropdown.png" style="max-width:100%;"></a>
    </p>
</details>

3. As a user I want to get more detailed look once I click on the recipe. 
    * Users get more specific details on the relevant recipe when they click the recipe button on the bottom of the card deck. 

4. As a user I want to be able to add my own recipes so I can use this website as a one stop shop for all my recipes.
    * Users who are logged in can add their own recipes. When they click the My Recipes tab, they are presented with a page full of their own recipes only. 

<details>
    <summary>User Story Add Recipes<strong>(Click dropdown for images)</strong></summary>
    <p align="center">
    <img height="350" src="README/images/add_recipe.png" style="max-width:100%;"></a>
    </p>
    <p align="center">
    <img height="350" src="README/images/my_recipes.png" style="max-width:100%;"></a>
    </p>
</details>

5. As a user I want to be able to delete or update/edit the recipes I added to the website.
    * Users who are logged in can edit and delete their own recipes only.
<details>
    <summary>User Story Edit/Delete<strong>(Click dropdown for images)</strong></summary>
    <p align="center">
    <img height="350" src="README/images/edit_delete_button.jpg" style="max-width:100%;"></a>
    </p>
    <p align="center">
    <img height="350" src="README/images/delete_recipe.png" style="max-width:100%;"></a>
    </p>
     <p align="center">
    <img height="350" src="README/images/edit_recipe.png" style="max-width:100%;"></a>
    </p>
</details>

6. As a user I want to easily understand the purpose of the site and learn what the owner’s beliefs are.
    * Reason for the About page so the user can get a better understanding of the app and the brand.

7. As a site owner, I want to ensure my website is secure, and I want to keep a dataset of my users.
    * Reason For Login/Registration. 

8. As a site owner i want to be able to control who can delete content as part of the crud functionality requirements. 
    
    * One of the main reasons for creating the authentication was to stop someone coming onto my site and deleting all the recipes. Their is an if statement set up which protects the content being deleted unless the user is the author of that recipe. 

<details>
    <summary>User Story If Statement<strong>(Click dropdown for images)</strong></summary>
    <p align="center">
    <img height="350" src="README/images/if_statement.png" style="max-width:100%;"></a>
    </p>
</details>

## Defensive Design with Authentication
I tested the defensive design of the website in the video i have uploaded below. 

Pages like 'My Recipes', 'Add Recipes', 'Edit Recipes' required session login. I tested the website by typing the url of those pages into the address bar and as planned i was greeted with the access denied page. 
I also tested if i could access the 'Login' page whilst logged, and as planned i was redirected away from the 'Login' page. 
I also tested imputting incorrect data into the login and registration pages and the correct reponses were rendered. 


<a href="https://www.youtube.com/watch?v=rG6XinYr78A&feature=youtu.be"><img src="README/images/youtube_video.png" max-width="50%"></a>