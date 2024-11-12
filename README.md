<!--https://github.com/darsaveli/Readme-Markdown-Syntax-->

### Collaborators:
* **[Lochlann O Neill](https://github.com/lochlannoneill)**
  
-----
  
### Running the project

1. Install **boto3**
   ```bash
   pip install boto3

2. Install **tabulate** for enhanced terminal output.
   ```bash
   pip install tabulate

3. Include user information in src/config/passwords.txt or register a new account during runtime.  
   See example template below ("Name", "Password", "Access Key", "Secret Key").
   ```bash
   David   12345pass   AKIKAOD798  PPB7952+AmaYUd+824nmW
   John    aaaaaaaaa   AKOP67NKAF  CpA9752SDF+709+fa09faAfG
   Joan    bcbcbcddddddd   AIL67NK8NM  KMALF75+95mml+7+89052

4. Execute the application
   ```bash
   python -m src.app
