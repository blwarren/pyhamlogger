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

### Using Poetry

To install PyHamLogger using [Poetry](https://python-poetry.org/), follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/blwarren/pyhamlogger.git
   cd pyhamlogger
   ```

2. Install the dependencies:

   ```bash
   poetry install
   ```

3. Activate the virtual environment:

   ```bash
   poetry shell
   ```

4. Run the application:

   ```bash
   python main.py
   ```

### Using pip

Alternatively, you can install the dependencies using `pip`:

1. Clone the repository:

   ```bash
   git clone https://github.com/blwarren/pyhamlogger.git
   cd pyhamlogger
   ```

2. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:

   ```bash
   python main.py
   ```

## Usage

After installing the dependencies, you can start the application by running:

```bash
python main.py
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