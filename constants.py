## -----------------------------------------------------------------------------
## Python Scripts                                     scriptarium/[constants.py]
## (c) balarabe@protonmail.com
## -----------------------------------------------------------------------------

# file extensions of source code and other text files
text_file_exts = [
    'LICENSE',   '.asm',      '.asn',             '.asp',         '.aspx',
    '.bas',      '.bat',      '.c',               '.cb12.depend', '.cbp',
    '.cc',       '.cfg',      '.classpath',       '.clj',         '.cljs',
    '.cls',      '.clw',      '.cpp',             '.cs',          '.csproj',
    '.css',      '.csv',      '.ctl',             '.ctp',         '.cxx',
    '.def',      '.dep',      '.dpr',             '.dsp',         '.dsw',
    '.fd',       '.frm',      '.gitignore',       '.go',          '.go2',
    '.go_',      '.gohtml',   '.gradle',          '.gson',        '.h',
    '.hc',       '.hh',       '.hhc',             '.hhk',         '.hhp',
    '.hpp',      '.hs',       '.hta',             '.htm',         '.html',
    '.hxx',      '.iml',      '.in_less',         '.jade',        '.java',
    '.java_',    '.jcl',      '.js',              '.json',        '.jsonp',
    '.kt',       '.layout',   '.less',            '.log',         '.mak',
    '.manifest', '.md',       '.meta',            '.odl',         '.pas',
    '.pdm',      '.ph',       '.php',             '.pl',          '.plg',
    '.pm',       '.prefs',    '.pro',             '.project',     '.properties',
    '.py',       '.rb',       '.rc',              '.rc2',         '.reg',
    '.resx',     '.rgon',     '.rs',              '.rules',       '.sass',
    '.scss',     '.settings', '.sh',              '.shtml',       '.sln',
    '.sql',      '.sqlpg',    '.svg',             '.ters',        '.thin',
    '.tlh',      '.tli',      '.toml',            '.ts',          '.txt',
    '.user',     '.vbp',      '.vbw',             '.vcp',         '.vcproj',
    '.vcw',      '.vcxproj',  '.vcxproj.filters', '.workspace',   '.xaml',
    '.xhtml',    '.xml',      '.xs',              '.xsd',         '.xsx',
    '.yml',
]

# file patterns to ignore when zipping or unzipping files (regular expressions)
zip_ignore = [
    '.*\.data$',
    '.*\.dbe$',
    '.*\.exe$',
    '.*\.log$',
    '.*\.out$',
    '.*\.rlog$',
    '.*\.tmp$',
    '.*\.ttf$',
    '.*\.zip$',
    '.*debug.test$',
]

# end