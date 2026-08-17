from langchain_text_splitters import RecursiveCharacterTextSplitter

splitter=RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

def chunker(pages):
    chunks=[]
    i=0
    for page in pages:
        page_chunks=splitter.split_text(page["text"])
        for chunk in page_chunks:
            i+=1
            chunks.append(
                {
                    "chunk_id":i,
                    "page":page["page"],
                    "chunk":chunk
                }
            )

    return chunks