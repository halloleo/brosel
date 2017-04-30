`brosel`
=========

*Select the right browser for a URL - A script and macOS wrapper app*

The wrapper can be used as OS-wide Default web browser. The rules are
customisable through a config file. The wrapper app is generated with

### Installation

Generate the wrapper app with [Platypus](http://sveinbjorn.org/platypus). You
have to install only the command line tools, which you can do via
[Homebrew](https://brew.sh/) (`brew install platypus`). The profile to create
the app is stored in `brosel.platypus`. So after downloading/cloning this
repository, `cd` into the repo directory and issue the following command in a
shell:

    platypus -P brosel.platypus /Applications/brosel.app

*Note 1:* Paths in the the profile are *relative*, so you need to be in the
repository directory so tat platypus finds the script `brosel.py` and the
dependency `yaml`.

*Note 2:* You can save the application to any directory you want,
`/Applications/brosel.app` is only the standard option.

### How to configure the custom rules

`brosel` looks for its configuration in the file `~/.brosel` and then in the
file `~/Library/Application Support/brosel.yaml`. The first one found `brosel`
reads as a [YAML](http://www.yaml.org/spec/1.2/spec.html) file. A sample
config looks like this:

```YAML
basic:
    browser_id: open -a "Google Chrome.app" %s
rules:
-   # rule for local files
    browser_id: open -a Safari.app %s
    url_pattern: '^file://'
-   # rule for urls from emacs
    browser_id: open -a Firefox.app %s
    url_pattern: ^emacs-
    url_replace: ''
```

In the **`basic`** section you can define the default browser to use if no
rules applies. Use the key `browser_id`. The value is the
[`open`](https://developer.apple.com/legacy/library/documentation/Darwin/Reference/ManPages/man1/open.1.html)
statement you would use on command line to open the URL with the desired
browser. In this string `%s` stands for the position where the URL will be
inserted.

In the **`rules`** section you define the rules: Each rules can contain the following keys:

key | meaning | required ?
----|---------|-----------
`browser_id` | The browser to use | yes
`url_pattern` | The regular expression the URL as to match | yes
`url_replace` | A replacement for the URL if the URL should be changed | no

Notes: `url_pattern` and `url_replace` use the [Python variant of regular expression](https://docs.python.org/2/library/re.html).

### How to set `brosel` as Default web browser

In **System Preferences** go to the **General** pane and se;ect nrosel.app. -
Not: *In order to appear in this list you might have run brsoel.app at least
once via double-click.*

### Credits:

* Thanks to [Sveinbjorn Thordarson](http://sveinbjorn.org/) for Platypus.
* Thanks to the [PyYaml community](http://pyyaml.org/) for [PyYaml](http://pyyaml.org/wiki/PyYAML).
