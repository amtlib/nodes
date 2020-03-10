# Nodes

## Requirements
1. unittest

## Installation
1. Create virtalenv
```
    python3 -m venv venv
```
2. Activate venv
    - Ubuntu
    ```
        source venv/bin/active
    ```
    - Windows
    ```
        cd venv/Scripts
        activate.bat
        cd ../..
    ```

3. Install requirements
```
    pip install -r requirements.txt
```
## How to run?
1. BST Tree
```
    cd bst
    python app.py
```
2. Random Tree
```
    cd random_tree
    python app.py
```
## Running tests
1. BST
```
    cd bst
    python test_tree.py
```
2. Random Tree
```
    cd random_tree
    python test_node.py
```