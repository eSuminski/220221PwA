package dev.revature.importing;

// the import starts at my root java folder in main, works its way down to the class itself
import dev.revature.importfrom.ImportParent;

public class ImportChild extends ImportParent {
    public ImportChild(String parentString) {
        super(parentString);
    }

    public static void main(String[] args) {
        ImportChild child = new ImportChild("this is my string");
    }
}
