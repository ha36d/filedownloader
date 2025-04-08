# File Downloader

This script fetches and downloads all public files with a specific extension from a given base URL. It also renames the downloaded files by decoding URL-encoded characters.

## Features

- Fetches one-level URLs matching a specific pattern from a base URL.
- Downloads files with a specified extension (default: `.pdf`).
- Renames downloaded files by decoding URL-encoded characters.

## Requirements

Install the required Python packages using:

```bash
pip install -r [requirements.txt](http://_vscodecontentref_/1)
```

## How It Works

* Fetch URLs: The script fetches all one-level URLs from the base URL that match the specified pattern.
* Download Files: For each URL, it downloads files with the specified extension.
* Rename Files: After downloading, it renames the files by decoding any URL-encoded characters.

## Example

If the base URL is `https://example.com/` and the pattern is `folder/`, the script will:

* Fetch URLs like `https://example.com/folder/subfolder/`.
* Download files like `document.pdf` from those URLs.
* Rename files like `document%20name.pdf` to `document name.pdf`.

## License

This project is licensed under the MIT License.
