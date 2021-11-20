A service to display a quick summary of a project on GitHub.

# Usage 📖

`{repo}` is the name of the repository.
`{user}` is the name of the user.

```
[![Project Card](https://project-card-app.herokuapp.com/project_card/{user}/{repo})](https://github.com/{user}/{repo})
```

An example of the project card:

Here,

`{repo}` : `linux`

`{user}` : `torvalds`

[![Project Card](https://project-card-app.herokuapp.com/project_card/torvalds/linux)](https://github.com/torvalds/linux)

## Themes 🎨

You can change the theme of the project card by adding a `theme` parameter to the URL.

```
[![Project Card](https://project-card-app.herokuapp.com/project_card/{user}/{repo}?theme={theme})](https://github.com/{user}/{repo})
```

### Available Themes

- `dark-blue` (default)

[![Project Card](https://project-card-app.herokuapp.com/project_card/torvalds/linux?theme=dark-blue)](https://github.com/torvalds/linux)

- `light`

[![Project Card](https://project-card-app.herokuapp.com/project_card/torvalds/linux?theme=light)](https://github.com/torvalds/linux)

- `violet`

[![Project Card](https://project-card-app.herokuapp.com/project_card/torvalds/linux?theme=violet)](https://github.com/torvalds/linux)

More themes coming soon ...

## Any contributions are welcome 😀
