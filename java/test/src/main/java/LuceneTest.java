import org.apache.lucene.analysis.core.WhitespaceAnalyzer;
import org.apache.lucene.analysis.standard.StandardAnalyzer;
import org.apache.lucene.document.Document;
import org.apache.lucene.document.Field;
import org.apache.lucene.index.DirectoryReader;
import org.apache.lucene.index.IndexReader;
import org.apache.lucene.index.IndexWriter;
import org.apache.lucene.index.IndexWriterConfig;
import org.apache.lucene.index.Term;
import org.apache.lucene.search.IndexSearcher;
import org.apache.lucene.search.Query;
import org.apache.lucene.search.ScoreDoc;
import org.apache.lucene.search.TermQuery;
import org.apache.lucene.search.TopDocs;
import org.apache.lucene.store.Directory;
import org.apache.lucene.store.RAMDirectory;
import org.apache.lucene.util.Version;
import org.apache.lucene.document.FieldType;

import java.io.IOException;

public class LuceneTest {

    public static void main(String[] argc) throws IOException {
        System.out.println("Index generating");
        Directory index = new RAMDirectory();
        WhitespaceAnalyzer whitespaceAnalyzer = new WhitespaceAnalyzer(Version.LUCENE_43);
        StandardAnalyzer analyzer = new StandardAnalyzer(Version.LUCENE_43);
        IndexWriterConfig conf = new IndexWriterConfig(Version.LUCENE_43, analyzer);
        IndexWriter indexWriter = new IndexWriter(index, conf);

        System.out.println("Document buliding");
        FieldType fieldType = new FieldType();
        fieldType.setIndexed(true);
        fieldType.setStored(true);
        fieldType.setTokenized(true);
        Document doc = new Document();
        doc.add(new Field("name", "lisa df", fieldType));
        doc.add(new Field("name", "yyy", fieldType));
        indexWriter.addDocument(doc);
        indexWriter.close();
        System.out.println("Index generate done");

        System.out.println("Index searching");
        IndexReader reader = DirectoryReader.open(index);
        IndexSearcher searcher = new IndexSearcher(reader);

        System.out.println("Building query");
        Query query = new TermQuery(new Term("name", "lisa"));
        TopDocs topDocs = searcher.search(query, 10);
        System.out.println("Index searching done");

        System.out.println("Searching resulet show:");
        Document resultDoc;
        ScoreDoc[] docs = topDocs.scoreDocs;
        for(int i = 0;i < topDocs.totalHits; i++) {
            resultDoc = searcher.doc(docs[i].doc);
            System.out.println(resultDoc.get("name"));
        }
        System.out.println("done");
    }
}
