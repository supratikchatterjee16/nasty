package factserver.core;

import edu.stanford.nlp.coref.CorefCoreAnnotations;
import edu.stanford.nlp.coref.data.CorefChain;
import edu.stanford.nlp.ie.util.RelationTriple;
import edu.stanford.nlp.international.Language;
import edu.stanford.nlp.io.IOUtils;
import edu.stanford.nlp.io.RuntimeIOException;
import edu.stanford.nlp.ling.CoreAnnotation;
import edu.stanford.nlp.ling.CoreAnnotations;
import edu.stanford.nlp.ling.CoreLabel;
import edu.stanford.nlp.ling.IndexedWord;
import edu.stanford.nlp.pipeline.*;
import edu.stanford.nlp.semgraph.SemanticGraph;
import edu.stanford.nlp.semgraph.SemanticGraphCoreAnnotations;
import edu.stanford.nlp.semgraph.SemanticGraphEdge;
import edu.stanford.nlp.semgraph.semgrex.SemgrexMatcher;
import edu.stanford.nlp.semgraph.semgrex.SemgrexPattern;
import edu.stanford.nlp.stats.ClassicCounter;
import edu.stanford.nlp.stats.Counter;
import edu.stanford.nlp.stats.Counters;
import edu.stanford.nlp.trees.GrammaticalRelation;
import edu.stanford.nlp.trees.UniversalEnglishGrammaticalRelations;
import edu.stanford.nlp.util.*;
import edu.stanford.nlp.util.logging.Redwood;
import edu.stanford.nlp.util.logging.RedwoodConfiguration;

import edu.stanford.nlp.naturalli.NaturalLogicAnnotations;

import java.io.File;
import java.io.IOException;
import java.io.PrintStream;
import java.util.*;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;
import java.util.concurrent.atomic.AtomicInteger;
import java.util.stream.Collectors;


public class RelationExtractor{
	private static StanfordCoreNLP pipeline;
	public RelationExtractor(){
		Properties props = new Properties();
		props.setProperty("annotators","tokenize,ssplit,pos,lemma,ner,parse,depparse,coref,kbp,natlog,openie");
		props.setProperty("openie.resolve_coref","true");
		props.setProperty("coref.md.type", "dep");  // so we don't need the `parse` annotator
        props.setProperty("coref.mode", "statistical");  // explicitly ask for scoref
		props.setProperty("tokenize.class", "PTBTokenizer");
		props.setProperty("tokenize.language", "en");
		RedwoodConfiguration.current().clear().apply();
		pipeline = new StanfordCoreNLP(props);
	}
	
	public String parse(String document){
		StringBuffer res = new StringBuffer();
		
		// Annotate the document
		Annotation ann = new Annotation(document);
		this.pipeline.annotate(ann);
		
		// Get the extractions
		boolean empty = true;
		for (CoreMap sentence : ann.get(CoreAnnotations.SentencesAnnotation.class)) {
			for (RelationTriple extraction : sentence.get(NaturalLogicAnnotations.RelationTriplesAnnotation.class)) {
			// Print the extractions
				res.append(extraction.subjectGloss()+","+extraction.relationGloss()+","+extraction.objectGloss()+","+extraction.confidenceGloss()+"\n");
				empty = false;
			}
		}
		//System.out.println(res);
		return res.toString();
	}
	
	public static void main(String[] args){
		RelationExtractor ext  = new RelationExtractor();
		String res = "";
		res = ext.parse("Pakistan's information ministry published - but subsequently deleted - a video showing the blindfolded pilot, who could be heard requesting water, just after he had been captured. In later footage, he could be seen sipping tea from a cup without a blindfold. India's foreign ministry later issued a statement demanding the release of its fighter pilot and condemning the images, describing them as a \"vulgar display of an injured personnel\". The pilot's family have not yet commented on the events, but footage shared on social media shows passengers on a Chennai to Delhi flight cheering his parents. ");
		System.out.println(res);
	}
}