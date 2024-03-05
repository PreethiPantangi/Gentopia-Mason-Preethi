from typing import AnyStr
from pathlib import Path
import PyPDF2
from gentopia.tools.basetool import *


class ReadPDFArgs(BaseModel):
    file_path: str = Field(..., description="query relating to reading a pdf with file name")


class ReadPDF(BaseTool):
    """Tool that adds the capability to read a PDF file."""

    name = "read_pdf"
    description = ("A tool that is used to read a pdf and provide information."
                   "Input should be a query with pdf to be read.")

    args_schema: Optional[Type[BaseModel]] = ReadPDFArgs

    def _run(self, file_path: AnyStr) -> str:
        with open(str(file_path), 'rb') as pdf_file:
            reader = PyPDF2.PdfReader(pdf_file)
            information = ""
            for num in range(len(reader.pages)):
                page = reader.pages[num]
                information += page.extract_text()
        
        return information

    async def _arun(self, *args: Any, **kwargs: Any) -> Any:
        raise NotImplementedError


if __name__ == "__main__":
    ans = ReadPDF()._run("Attention for transformer")
    print(ans)
