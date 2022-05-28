Documentation
=============

To generate documentation for new/existing python files, run the following commands into the terminal.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Installation
---------------

Install sphinx and its corresponding theme on your system in order to run below commands.

.. code-block::

    pip install sphinx

.. code-block::

    pip install furo

.. note::
    
    All of the commands in the following steps must be run from the **docs** directory. It houses all documentation-related files. The configuration file "conf.py," custom templates, and all other rst files are located in the *soucre* directory under the *docs* directory.

.. code-block:: text

    Elves
    |- __init__.py
    |- module1.py
    |- module2.py
    |- tests
    |- docs
        |- build                   - Contains all HTML-related files
        |- soucre                  - Contains conf.py, custom templates, and rst files
            |- _templates
            |- api                 - Contains all of the project's generated rst files
            |- conf.py
            |- index.rst


2. Generate rst files
---------------------

To generate rst files for the respective package. It generates rst files in the source/api directory.

.. code-block::

    sphinx-apidoc -fMeT -t source/_templates -o source/api .. ../conftest.py

``-f`` : Force overwriting of any existing generated files.

``-M`` : Put module documentation before submodule documentation.

``-e`` : Put documentation for each module on its own page.

``-T`` : Do not create a table of contents file.

``-t`` : The template tag specifies the templates directory.

``source/_templates`` : Custom templates for packages and modules is included in this directory.

``-o`` : The output option specifies the output directory.

``source/api`` : Directory containing all of the project's generated rst files.

``..`` : The parent directory is searched for Python modules.

``../conftest.py`` : This file will be ignored when producing rst files for the python modules.

.. note::
    
   The ``-f`` option will overwrite all previously generated files. As a result, don't include any hard-coded rst files in the source/api directory. Only the generated rst files are stored in this directory.

3. To clean generated html files
--------------------------------

To remove all files from the build directory. This deletes all of the html files that were previously created.

.. note::

    To generate documentation for new files, this command must be executed prior to the make html command.

.. code-block::
    
    make clean

4. Generate html files
----------------------

To generate html files for the respective rst files. This will generate a website version of your documentation and place it in the build/html directory.

.. code-block::

    make html