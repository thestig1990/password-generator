# Password generator

Utility for generating passwords according to a given template that supports the CLI interface.

## CLI options

The script supports the following CLI options:

- **[ -n ]** - Set length of password and generate random password
                    from set {small lateral ASCII, big lateral ASCII, digit}
- **[ -t, --template ]** - Set template for generate passwords *(for future development)*
- **[ -f, --file ]** - Getting list of patterns from file and generate for each random password *(for future development)*
- **[ -c, --count ]** - Number of passwords
- **[ -v, --verbose ]** - Verbose mode (-v |-vv |-vvv ) *(for future development)*
- **[ -S, --set ]** - Character set
- **[ -p, --permute ]** - Randomly permute characters of password *(for future development)*

## Example 1. One password

Run script from CLI with arguments:
```CLI
python password_generator.py -n 12 -c 1 -S xyz
```

Input data:
```CLI
Use characters from set {small lateral ASCII, big lateral ASCII, digit, punctuation}? (y/yes): yes
```

Output data:
```CLI
Password: /2hEpf|7!%*E
```

## Example 2. Set of passwords

Run script from CLI with arguments:
```CLI
python password_generator.py -n 10 --count 3 --set xyz 
```

Input data:
```CLI
Use characters from set {small lateral ASCII, big lateral ASCII, digit, punctuation}? (y/yes): yes
```

Output data:
```CLI
List of passwords: ['sWKb`[qf5K', 'H$+}x]g4#c', 'ZJp;ia/)d@']
```