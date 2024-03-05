from typing import AnyStr
from pathlib import Path
import PyPDF2
from gentopia.tools.basetool import *


class ReadPDFArgs(BaseModel):
    query: str = Field(..., description="query relating to reading a pdf with file name")


class ReadPDF(BaseTool):
    """Tool that adds the capability to read a PDF file."""

    name = "read_pdf"
    description = ("A tool that is used to read a pdf and provide information."
                   "Input should be a query with pdf to be read.")

    args_schema: Optional[Type[BaseModel]] = ReadPDFArgs

    def _run(self, file_path: AnyStr) -> str:
        read_file = Path(file_path)
        print(read_file)
        with open(read_file, 'rb') as pdf_file:
            reader = PyPDF2.PdfFileReader(pdf_file)
            information = ""
            for num in range(reader.numPages):
                page = reader.getPage(num)
                information += page.extractText()
        return information
        # return "This will read the pdf and return information!"

    async def _arun(self, *args: Any, **kwargs: Any) -> Any:
        raise NotImplementedError


if __name__ == "__main__":
    ans = ReadPDF()._run("Attention for transformer")
    print(ans)
