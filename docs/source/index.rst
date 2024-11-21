.. CLAS documentation master file, created by
   sphinx-quickstart on Thu Nov 21 15:42:45 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to CLAS Documentation!
==================

Add your content using ``reStructuredText`` syntax. See the
`reStructuredText <https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html>`_
documentation for details.


.. toctree::
   :maxdepth: 2
   :caption: Contents:
   
   project_info
   getting_started
   usage
   architecture
   api_reference


Project Information
===================

Welcome to the CLAS (Chef: Light and Shadow) project!

**Project Overview:**
CLAS is a community-driven platform that allows users to share their unique and personal recipes. Unlike traditional recipe platforms, CLAS emphasizes creativity and individuality, giving everyone a chance to showcase their hidden culinary talents.

**Key Objectives:**
- Provide a platform for sharing unique recipes.
- Build a vibrant cooking community.
- Promote creativity and exploration in cooking.

**Why CLAS?**
Most recipe platforms focus on standardized recipes. CLAS fills the gap by providing a space for personal and creative recipes to thrive.


Getting Started
===============

This section guides you through the initial steps to use and contribute to the CLAS project.

**1. Installation**
- Clone the repository:



Usage
=====

Learn how to use the features of CLAS effectively.

**1. Uploading a Recipe**
- Navigate to the "Upload Recipe" section.
- Fill in the recipe name, ingredients, and instructions.
- Add an image of the dish.
- Submit your recipe to share it with the community.

**2. Searching for Recipes**
- Use the search bar to find recipes by ingredients or keywords.
- Filter results by cuisine type or user ratings.

**3. Interacting with the Community**
- Leave comments and feedback on other users' recipes.
- Rate recipes to help others discover great content.


Architecture
============

Understand the technical design of the CLAS project.

**1. System Overview**
- The CLAS platform is built using the Django framework.
- The frontend uses Bootstrap for a responsive and user-friendly interface.

**2. Components**
- **Backend:** Django with RESTful APIs for data handling.
- **Frontend:** HTML, CSS, and JavaScript for rendering the UI.
- **Database:** PostgreSQL for storing user data, recipes, and feedback.

**3. Key Modules**
- **Recipe Management:** Handles recipe uploads, updates, and deletions.
- **Search and Recommendation:** Provides recipe search and personalized recommendations.
- **Community Features:** Includes comments, ratings, and feedback systems.


API Reference
=============

Explore the available APIs for the CLAS platform.

**1. Recipe APIs**
- **GET /api/recipes/**  
  Retrieve a list of all recipes.  
  **Parameters:**  
  - `search` (optional): Filter recipes by keyword.

- **POST /api/recipes/**  
  Create a new recipe.  
  **Payload:**  
  ```json
  {
      "name": "Recipe Name",
      "ingredients": "List of ingredients",
      "instructions": "Step-by-step instructions",
      "image": "Image URL"
  }


