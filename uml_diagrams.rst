source : https://gist.github.com/HarshaVardhanBabu/9a47db9e33cf06e9e1e917520bb54056

Requirements
=============

1. Install ``Pylint`` from `Install <https://www.pylint.org/#install>`_. If you have anaconda already installed use ``pip install -U pylint`` to update the ``Pylint`` so that ``pyreverse`` is added to the scripts folder.
2. You need to install Graphviz as the pyreverse generates the UML diagrams in dot format and needs the dot.exe provided by Graphviz. Once Graphviz is installed make sure the bin folder is added to the ``PATH`` variable so that pyreverse can find it at run time. "the command pyreverse generates the diagrams in all formats that graphviz/dot knows." (`Reference <http://www.logilab.org/blogentry/6883>`_
3. Now add the path of python modules for which you want to generate the documentation to PYTHONPATH.
4. Use pyreverse -S <modulename> to generate dot files in the current folder
  
   Usage:
  
    pyreverse [options] <packages>

    create UML diagrams for classes and modules in <packages>


    Options:
      -h, --help            show this help message and exit
      -f <mode>, --filter-mode=<mode>
                            filter attributes and functions according to
                            <mode>. Correct modes are :
                            'PUB_ONLY' filter all non public attributes
                            [DEFAULT], equivalent to PRIVATE+SPECIAL_A
                            'ALL' no filter                             'SPECIAL'
                            filter Python special functions
                            except constructor                             'OTHER'
                            filter protected and private
                            attributes [current: PUB_ONLY]
      -c <class>, --class=<class>
                            create a class diagram with all classes related to
                            <class>; this uses by default the options -ASmy
                            [current: none]
      -a <ancestor>, --show-ancestors=<ancestor>
                            show <ancestor> generations of ancestor classes not in
                            <projects>
      -A, --all-ancestors   show all ancestors off all classes in <projects>
      -s <ass_level>, --show-associated=<ass_level>
                            show <ass_level> levels of associated classes not in
                            <projects>
      -S, --all-associated  show recursively all associated off all associated
                            classes
      -b, --show-builtin    include builtin objects in representation of classes
      
      -m [yn], --module-names=[yn] 
                            include module name in representation of classes
      -k, --only-classnames 
                            don't show attributes and methods in the class boxes;   this disables -f values
      -o <format>, --output=<format>
                            create a *.<format> output file if format available. [current: dot]
      --ignore=<file[,file...]> 
                            Add files or directories to the blacklist. They should be base names, not paths. [current: CVS]
      -p <project name>, --project=<project name>  
                            set the project name. [current: none]
5. Once the dot files are generated use the following to generate the output in one of the formats available 
  Usage:
    
    dot -Tpdf <dotfilename> -o output.pdf
    
    dot -Txxx shows all the available output formats
