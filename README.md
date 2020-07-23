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
    
3. As a user I want to get more detailed look once I click on the recipe title/image.
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









