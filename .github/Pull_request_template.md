## Description
- This PR adds a new feature that allows users to search for recipes by ingredients.
- It also fixes a bug where the recipe upload page would crash if an image was not provided.

## Changes
- Added a search bar on the main page that allows users to search recipes by ingredients.
- Updated the recipe model to include a list of ingredients for search functionality.
- Fixed a bug in the recipe upload feature where omitting an image would cause the page to crash.

## Motivation and Context
- The new search feature improves the user experience by making it easier to find recipes based on available ingredients.
- The bug fix ensures that users can upload recipes without needing to attach an image, improving accessibility.

## Checklist:
- [x] I have ensured that the code functions correctly.
- [x] I have written tests and verified that all tests pass.
- [x] I have updated documentation to reflect the changes.
