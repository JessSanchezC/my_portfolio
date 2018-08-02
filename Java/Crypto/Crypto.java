import java.util.*;
public class Crypto {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        //take in string to be encrypted
        System.out.print("Enter message to encrypt: ");
        String text=input.nextLine();

        //take the value or key
        System.out.print("Enter a number to shift the message letters (it can be a negative value): ");
        int key=input.nextInt();

        //take the grouping size
        System.out.print("Enter the grouping size of the encrypted message: ");
        int size=input.nextInt();

        //encrypt message
        String encryptedText=encryptString(text,key,size);

        System.out.println("\n***********\n");
        System.out.println("The encrypted message is: \n"+encryptedText);

        //decrypt message

        String ungrouped=ungroupify(encryptedText);
        String decrypted=decrypt(ungrouped,key);

        System.out.println("\n***********\n");
        System.out.println("The decrypted message is: \n"+decrypted);
        System.out.println("\n***********");

    }

    public static String normalizeText(String text1){

        //1. Removes all the spaces from your text
        String normalizedText=text1.replaceAll(" ","");

        //2. Remove any punctuation (. , : ; ’ ” ! ? ( ) )
        normalizedText=normalizedText.replaceAll("[.,:;'\"!?()]","");

        //3. Turn all lower-case letters into upper-case letters
        normalizedText=normalizedText.toUpperCase();

        // 4. Return the result.
        return normalizedText;

        //Checked, working OK
    }

    public static String ceasarify(String text3, int key){
        /*
        The function should return a string, which is the input string encrypted with the Caesar cypher
        using the shift value passed in its second argument. You may assume that the input string is normalized.

        -Note that the alphabet “wraps around”, so with a shift value of +1 the “Z” in ZOOS became an A.
        -You can also have negative shift values, which cause the alphabet to previous letters.
        With a -1 shift, the string “ILIKEAPPLES” would turn into “HKHJDZOOKDR.”

        */
        String alphabet=shiftAlphabet(0);
        String shiftedAlfabet=shiftAlphabet(key);
        String ceasarifiedText="";

        int position=text3.length()-1;
        //to test: System.out.println(alphabet+"\n"+shiftedAlfabet+"\n"+position);

        while (position>=0) {
            ceasarifiedText=shiftedAlfabet.charAt(alphabet.indexOf(text3.charAt(position)))+ceasarifiedText;
            position--;
        }

        //to test:System.out.println("?"+ceasarifiedText);

        return ceasarifiedText;

        //checked OK

    }

    public static String shiftAlphabet(int shift) {
        /*
        Method provided (copy/paste).
        This function takes one argument, an integer to specify the shift value, and returns a string,
        which is the uppercase alphabet shifted by the shift value.
        So if you call shiftAlphabet(2), you will get back the following string: “CDEFGHIJKLMNOPQRSTUVWXYZAB”
         */
        int start = 0;
        if (shift < 0) {
            start = (int) 'Z' + shift + 1;
        } else {
            start = 'A' + shift;
        }
        String result = "";
        char currChar = (char) start;
        for(; currChar <= 'Z'; ++currChar) {
            result = result + currChar;
        }
        if(result.length() < 26) {
            for(currChar = 'A'; result.length() < 26; ++currChar) {
                result = result + currChar;
            }
        }
        return result;
    }

    public static String groupify(String text4,int size ){

        int position=size;

        //If there aren’t enough letters in the input string to fill out all the groups, you should “pad” the final group with x’s.
        //So groupify(“HITHERE”, 2) would return “HI TH ER Ex”.
        //You may assume that the input string is normalized.
        //Note that we use lower-case ‘x’ here because it is not a member of the (upper-case) alphabet we’re working with. If we used upper-case ‘X’ here we would not be able to distinguish between an X that was part of the code and a padding X.

        while (text4.length()%size!=0){
            text4=text4+"x";
        }

        //The function will return a string, which consists of the input string broken into groups
        //with the number of letters specified by the second argument.

        while (position<text4.length()){
            text4=text4.substring(0,position)+" "+text4.substring(position,text4.length());
            position=position+size+1;
        }

        return text4;
    }

    public static String encryptString(String text, int key, int size){

    //Call normalizeText on the input string.
    String normalizedText=normalizeText(text);

    //Call ceasarify to encrypt the normalizedText.
    String ceasarifiedText=ceasarify(normalizedText,key);

    //Call groupify to break the cyphertext into groups of size letters.
    String groupifiedText= groupify(ceasarifiedText,size);

    //Return the result
    return groupifiedText;
    }

    public static String ungroupify(String eText){

        //Returns the encrypted string without any spaces and "x"
        String ungroupedText=(eText.replaceAll(" ","")).replaceAll("x","");
        return ungroupedText;
    }

    public static String decrypt(String toDecrypt, int key){
        String decrypted="";
        String alphabet=shiftAlphabet(0);
        String shiftedAlfabet=shiftAlphabet(key);
        int position=toDecrypt.length()-1;

        while (position>=0) {
            decrypted=alphabet.charAt(shiftedAlfabet.indexOf(toDecrypt.charAt(position)))+decrypted;
            position--;
        }

        return decrypted;
    }

}
