Usage Instructions
==================

Follow the instructions below to effectively use the CLAS project tools and features:

Basic Usage
-----------

Once you have installed the CLAS platform (see :doc:`getting_started`), you can perform the following operations:

- **Launching the main application:**

  .. code-block:: bash

     python main.py

- **Analyzing data files:**

  .. code-block:: bash

     python main.py analyze --file data.csv

- **Running with a custom configuration:**

  .. code-block:: bash

     python main.py --config custom_config.yaml

Example Scenarios
-----------------

Here are some common use cases for the CLAS platform:

- **Scenario 1: Data Analysis**

  Use the following command to analyze a dataset and generate a report:

  .. code-block:: bash

     python main.py analyze --file data.csv --output report.txt

- **Scenario 2: Real-time Monitoring**

  Enable live data monitoring with:

  .. code-block:: bash

     python main.py monitor --source live_stream

- **Scenario 3: Debugging**

  Run the application in debug mode to get detailed logs:

  .. code-block:: bash

     python main.py --debug

Tips and Tricks
---------------

- Use the ``--help`` flag with any command to see available options:

  .. code-block:: bash

     python main.py --help

- Refer to the :doc:`api_reference` for advanced customization and integration.
