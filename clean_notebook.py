import nbformat

# Path to your notebook
notebook_path = "Cat_Dog_Classifier_Advanced (2).ipynb"
# Load notebook
with open(notebook_path, "r", encoding="utf-8") as f:
    nb = nbformat.read(f, as_version=4)

# Remove 'widgets' metadata if it exists
if "widgets" in nb.metadata:
    del nb.metadata["widgets"]

# Save cleaned notebook
with open(notebook_path, "w", encoding="utf-8") as f:
    nbformat.write(nb, f)

print("Notebook metadata cleaned for GitHub!")