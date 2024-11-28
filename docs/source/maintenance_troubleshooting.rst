Maintenance and Troubleshooting for CLAS
==========================================

Check for Updates
-----------------
- Regularly check for updates if you’re testing new features or bug fixes.
- Updates may be delivered via direct download or through your development environment.

Clear Temporary Data
--------------------
- If performance issues arise, clear temporary files (manually, if no in-app function exists).
- This can be done by locating and removing unused local files in the app directory.

App Crashes Frequently
-----------------------
- **Cause:** Bugs in the code or unhandled exceptions.
- **Fix:**
  - Review the logs for errors and fix them in the code.
  - Restart the app after clearing temporary data.
  - Test new features in isolated environments before integrating them.

Recipe Data Disappears
----------------------
- **Cause:** Issues with saving or loading data from the database.
- **Fix:**
  - Double-check the save/load functions in your code.
  - Ensure the app saves data to a persistent location.

Performance Slows Down
----------------------
- **Cause:** Inefficient queries or too much test data.
- **Fix:**
  - Optimize database queries.
  - Delete unnecessary dummy data.


