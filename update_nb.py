import json

file_path = "Learner_Template_Notebook_AML_and_MLOps_Project_(1)_(1) (1).ipynb"
with open(file_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

for cell in nb.get('cells', []):
    if cell.get('cell_type') == 'code':
        for i, line in enumerate(cell.get('source', [])):
            if 'GITHUB_USERNAME   =' in line:
                cell['source'][i] = 'GITHUB_USERNAME   = "harshitrathi14"                 # Your GitHub username\n'
            elif 'REPO_NAME         =' in line:
                cell['source'][i] = 'REPO_NAME         = "tourism-package-prediction"  # Repository name\n'

links_cell = {
  "cell_type": "markdown",
  "metadata": {},
  "source": [
    "## Project Links\n",
    "\n",
    "- **GitHub Repository**: https://github.com/harshitrathi14/tourism-package-prediction\n",
    "- **Streamlit Community Cloud App**: https://tourism-package-prediction-zrgfbaar4vmzucwyzawe7x.streamlit.app/\n"
  ]
}

nb['cells'].append(links_cell)

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=2)
