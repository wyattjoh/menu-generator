# Menu Generator

Easily create a stylized menu.

## menu.yaml

The format of the config file is as follows:

```yaml
name:                   # the name of the menu

date:                   # optional date of the event

fonts:
  title:                # true type font name of the title text
  body:                 # true type font name of the body text

courses:                # list of courses
  - name:               # name of the course
    items:              # list of menu items
      - name:           # name of food item
        description:    # description of food item
      # ...
  # ...
```
