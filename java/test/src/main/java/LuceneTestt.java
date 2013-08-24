import org.apache.lucene.analysis.core.WhitespaceAnalyzer;
import org.apache.lucene.analysis.standard.StandardAnalyzer;
import org.apache.lucene.document.Document;
import org.apache.lucene.document.Field;
import org.apache.lucene.document.FieldType;
import org.apache.lucene.index.DirectoryReader;
import org.apache.lucene.index.Fields;
import org.apache.lucene.index.IndexReader;
import org.apache.lucene.index.IndexWriter;
import org.apache.lucene.index.IndexWriterConfig;
import org.apache.lucene.index.SlowCompositeReaderWrapper;
import org.apache.lucene.index.Term;
import org.apache.lucene.index.Terms;
import org.apache.lucene.index.TermsEnum;
import org.apache.lucene.queryparser.classic.QueryParser;
import org.apache.lucene.queryparser.flexible.core.nodes.ProximityQueryNode;
import org.apache.lucene.search.BooleanClause;
import org.apache.lucene.search.BooleanQuery;
import org.apache.lucene.search.IndexSearcher;
import org.apache.lucene.search.PhraseQuery;
import org.apache.lucene.search.Query;
import org.apache.lucene.search.ScoreDoc;
import org.apache.lucene.search.TermQuery;
import org.apache.lucene.search.TopDocs;
import org.apache.lucene.search.WildcardQuery;
import org.apache.lucene.search.similarities.Similarity;
import org.apache.lucene.store.Directory;
import org.apache.lucene.store.RAMDirectory;
import org.apache.lucene.util.Version;

import java.io.IOException;
import java.util.HashSet;
import java.util.Iterator;

/**
 * Created with IntelliJ IDEA. User: lo Date: 8/19/13 Time: 10:34 AM To change this template use
 * File | Settings | File Templates.
 */
public class LuceneTestt {
    public static void main(String[] argc) throws IOException {
        System.out.println("Start Test");
        //Directory dir = new FSDirectory();
        Directory index = new RAMDirectory();
        StandardAnalyzer standardAnalyzer = new StandardAnalyzer(Version.LUCENE_43);
        WhitespaceAnalyzer whitespaceAnalyzer = new WhitespaceAnalyzer(Version.LUCENE_43);

        IndexWriterConfig conf = new IndexWriterConfig(Version.LUCENE_43, whitespaceAnalyzer);
        conf.setOpenMode(IndexWriterConfig.OpenMode.CREATE);

        IndexWriter indexWriter = new IndexWriter(index, conf);

        Document doc1 = new Document();
        Document doc2 = new Document();
        Document doc3 = new Document();

        FieldType fieldType = new FieldType();
        fieldType.setIndexed(true);
        fieldType.setStored(true);
        fieldType.setStoreTermVectors(true);
        fieldType.setStoreTermVectorPositions(true);

        Field field1 = new Field("name", "a x c b", fieldType);
        Field field2 = new Field("name", "c b x a", fieldType);
        Field field3 = new Field("name", "a c b a", fieldType);
        doc1.add(field1);
        doc2.add(field2);
        doc3.add(field3);
        indexWriter.addDocument(doc1);
        indexWriter.addDocument(doc2);
        indexWriter.addDocument(doc3);
        indexWriter.close();

        IndexReader indexReader = DirectoryReader.open(index);
        IndexSearcher indexSearcher = new IndexSearcher(indexReader);
//        Terms terms1 = SlowCompositeReaderWrapper.wrap(indexReader).terms("name"); //get all terms of field "nane" in indexReader
//        HashSet<Term> termSet = new HashSet<Term>();
//        HashSet<String> termStringSet = new HashSet<String>();
//        TermsEnum termsEnum = null;
//        termsEnum = terms1.iterator(termsEnum);
//
//        while(termsEnum.next() != null) {
//            termStringSet.add(termsEnum.term().utf8ToString());
//        }
//        Iterator itss = termStringSet.iterator();
//        while(itss.hasNext()) {
//            System.out.println(itss.next());
//        }
//
//        Fields fields = SlowCompositeReaderWrapper.wrap(indexReader).fields(); //get all field of indexReader
//        System.out.println();
//        Iterator<String> iteratorfield = fields.iterator();//walk through fields
//        while(iteratorfield.hasNext()) {
//            String field = iteratorfield.next();
//            System.out.println("field: " + field);
//            Terms terms  = fields.terms(field);//get all terms of the field
//            termsEnum = terms.iterator(termsEnum);//walk through terms by TermsEnum
//            while(termsEnum.next() != null) {
//                System.out.println(termsEnum.term().utf8ToString());
//            }
//        }
        for(int i = 0;i < indexReader.maxDoc(); i++) {
            System.out.println(indexReader.document(i));
        }


        //Similarity.SloppySimScorer();
//        termsEnum = terms1.iterator(termsEnum);
//        while(termsEnum.next() != null) {
//            System.out.println("---");
//            System.out.println("term: " + termsEnum.term().utf8ToString().toString());
//            System.out.println("totalTermFreq: " + termsEnum.totalTermFreq());
//            System.out.println("docFreq: " + termsEnum.docFreq());
//          System.out.println("docOrder: " + termsEnum.ord());//order
//        }

//        TermsEnum termsEnum1 = null;
//        for(int i = 0; i < indexReader.maxDoc(); i++) {
//            fields = indexReader.getTermVectors(i);
//            for(String field : fields) {
//                System.out.println("---");
//                System.out.println("field: " + field);
//                Terms terms = fields.terms(field);
//                termsEnum1 = terms.iterator(termsEnum1);
//                while(termsEnum1.next() != null) {
//                    System.out.println("===");
//                    System.out.println("term: " + termsEnum1.term().utf8ToString().toString());
//                    System.out.println("totalTermFreq: " + termsEnum1.totalTermFreq());
//                    System.out.println("docFreq: " + termsEnum1.docFreq());
//                    System.out.println("docOrder: " + termsEnum1.ord());//order
//                    //System.out.println(termsEnum1.termState());
//                }
//            //System.out.println(indexReader.getTermVectors(i));
//            }
//        }

        //WildcardQuery wildcardQuery = new WildcardQuery();
        //ProximityQueryNode queryNode = new ProximityQueryNode();
        System.out.println("Searching and Showing result");
        PhraseQuery phraseQuery = new PhraseQuery();
        phraseQuery.setSlop(3);
        phraseQuery.add(new Term("name", "a"));
        phraseQuery.add(new Term("name", "b"));
        BooleanQuery booleanQuery = new BooleanQuery();
        Query query = new TermQuery(new Term("name", "b"));
        booleanQuery.add(query, BooleanClause.Occur.SHOULD);
        query = new TermQuery(new Term("name", "b"));
        booleanQuery.add(query, BooleanClause.Occur.SHOULD);
        booleanQuery.add(phraseQuery, BooleanClause.Occur.MUST);
//        QueryParser parser = new QueryParser(Version.LUCENE_43, "name", whitespaceAnalyzer);
//        parser.setPhraseSlop(1);
//        try {
//            query = parser.parse("b a");
//        } catch (Exception e) {
//            System.out.println("error");
//        }
//        System.out.println(query);
        TopDocs topDocs = indexSearcher.search(booleanQuery, 10);
        ScoreDoc[] scoreDoc = topDocs.scoreDocs;

        if (topDocs.totalHits == 0) {
            System.out.println("found no result");
        }
        Document resultDoc;
        for(int i = 0; i < topDocs.totalHits; i++) {
            //System.out.println(scoreDoc);
//            Fields fields = indexReader.getTermVectors(i);
//            Iterator iterator = fields.iterator();
//            while(iterator.hasNext()) {
                //System.out.println(iterator.next().toString());
//            }
            resultDoc = indexSearcher.doc(scoreDoc[i].doc);
            System.out.println(resultDoc.get("name") + "  " + scoreDoc[i].toString());
            //System.out.println(resultDoc);
        }
    }
}
