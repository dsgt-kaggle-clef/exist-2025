Using the below sexism prompt (a lot of FPs) but with analysis as well. The result should be the same as subsets_trial1

```
sexism_prompt = (
    "You are an expert in identifying the presence of sexism in video content. "
    "Your task is to assess whether the content of the video criticizes through marginalization, "
    "prejudice against women based on gender stereotypes, beliefs in male superiority, or misogynistic views."
    "Briefly describe and analyze the content of the video then label it as 'YES' if the video embodies or criticizes sexism."
    "Please respond strictly in the following JSON format:\n\n"
    '{\n'
    '  "description": "[Your one-sentence description of the video]",\n'
    '  "label": "YES" or "NO"\n'
    '  "analysis": "YES" or "NO"\n'
    '}\n\n'
    "Only return valid JSON. Do not include any explanations or extra text."
)
```