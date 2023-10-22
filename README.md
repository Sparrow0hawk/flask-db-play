# Flask Database Playground

A repository for exploring Flask, Flask-SqlAlchemy, and Alembic.

## Dev setup

This project is set up to use [hatch](https://hatch.pypa.io/latest/).

If you have `hatch` installed you can use the following commands during development:

- Running the test suite
  ```bash
  hatch run test
  ```

- Running linting and type checker (not changes applied)
  ```bash
  hatch run lint:all
  ```
  
- Running formatter (changes applied)
  ```bash
  hatch run lint:fmt
  ```
  
- Running the Flask development server
  ```bash
  hatch run app
  ```