from langchain_text_splitters import RecursiveCharacterTextSplitter

splitter=RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

def chunker(content:list[str]):
    chunks=[]
    for page in content:
        page_chunks=splitter.split_text(page["text"])
        for chunk in page_chunks:
            chunks.append(
                {
                    "page":page["page"],
                    "chunk":chunk
                }
            )

    return chunks