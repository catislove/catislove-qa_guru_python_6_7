import os
import zipfile



def test_archive_files():
    resource_folder = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'resources')
    archive_name = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'tmp')
    with zipfile.ZipFile(os.path.join("tmp", archive_name), "w") as archive:
        for file_name in os.listdir(resource_folder):
            file_path = os.path.join(resource_folder, file_name)
            archive.write(file_path, file_name)
    with zipfile.ZipFile(os.path.join("tmp", archive_name), "r") as archive:
        assert archive.testzip() is None
        assert "docs-pytest-org-en-latest.pdf" in archive.namelist()
        assert "file_example_XLSX_50.xlsx" in archive.namelist()
        assert "hello.zip" in archive.namelist()
        assert "username.csv" in archive.namelist()
    #os.remove(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'tmp'))

