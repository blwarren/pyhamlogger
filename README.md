# PyHamLogger

PyHamLogger is an open-source Python-based GUI application designed for logging ham radio contacts. Built with PyQt6, PyHamLogger provides a user-friendly interface to help amateur radio enthusiasts keep track of their contacts in a structured and efficient way.

This project is in very early stages of development. Do not rely upon this for reliable logging at this stage.

## Features (in progress)

- **Easy Logging**: Simple form to log contacts with fields for call sign, frequency, mode, signal report, and more.
- **Customizable Views**: Sort, filter, and search your log entries with ease.
- **Database Storage**: Store your logs locally with SQLite.
- **Export Functionality**: Export your logs to popular formats such as CSV and ADIF.
- **Cross-Platform**: Works on Windows, macOS, and Linux.

## Installation

Install [uv](https://docs.astral.sh/uv/getting-started/installation/) first.
PyHamLogger requires Python 3.12 or later (below 4.0).

### Install as a tool

From a local checkout:

```bash
git clone https://github.com/blwarren/pyhamlogger.git
cd pyhamlogger
uv tool install .
```

Alternatively, install directly from GitHub:

```bash
uv tool install git+https://github.com/blwarren/pyhamlogger.git
```

The GitHub command requires the uv packaging changes to be present on the remote branch.
If the command is not on your PATH after installation, run `uv tool update-shell`
and restart your shell.

### Development setup

```bash
git clone https://github.com/blwarren/pyhamlogger.git
cd pyhamlogger
uv sync --locked
uv run pyhamlogger
```

`uv sync` installs the application and development dependencies into `.venv`.
Commit `uv.lock` when dependencies change so development installs remain reproducible.

Run the tests and build the package with:

```bash
uv run pytest
uv build
```

## Usage

After installing as a tool, start the application from any directory:

```bash
pyhamlogger
```

## Contributing

Contributions are welcome! If you'd like to contribute to PyHamLogger, please follow these steps:

1. Fork the repository.
2. Create a new branch with a descriptive name for your feature or bug fix.
3. Make your changes and commit them with clear and concise commit messages.
4. Push your branch to your forked repository.
5. Submit a pull request with a detailed description of your changes.

Please make sure to adhere to the coding standards used in the project and to update the documentation as needed.

## License

PyHamLogger is licensed under the GNU General Public License v3.0. This means that you are free to use, modify, and distribute the software, provided that any modifications or derivative works are also licensed under the GPL v3.0.

```
Copyright (C) 2024 Bobby Warren

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program.  If not, see <https://www.gnu.org/licenses/>.
```

## Contact

If you have any questions, suggestions, or issues, feel free to open an issue on GitHub or contact the project maintainer:

- **Project Maintainer:** Bobby Warren
- **Email:** blwarren@gmail.com

## Acknowledgements

Thank you to all contributors and users of PyHamLogger. Your support helps make this project better with each release.

---

Happy logging, and 73!
