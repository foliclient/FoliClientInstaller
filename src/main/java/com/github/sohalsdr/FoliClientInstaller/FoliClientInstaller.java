package com.github.sohalsdr.FoliClientInstaller;

import org.apache.commons.io.FileUtils;
import java.io.*;
import java.net.URL;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.nio.file.StandardCopyOption;
import java.util.Scanner;

public class FoliClientInstaller {
    public static void main(String[] args) throws IOException {
        if(args.length == 0) {
            Scanner in = new Scanner(System.in);
            System.out.println("Type in the FULL FILE PATH of the minecraft directory where you want to install Foli Client!");
            String destFolderPath = in.nextLine();
            in.close();
            copyStuff(destFolderPath);
        } else {
            String destFolderPath = args[0];
            copyStuff(destFolderPath);
        }
    }

    public static void copyStuff(String destFolderPath) throws IOException {
        File destFolder = new File(destFolderPath);
        if(!destFolder.isDirectory()) {
            System.out.println(destFolderPath + " doesn't exist or isn't a folder!");
            System.exit(-1);
        }
        InputStream is = FoliClientInstaller.class.getResourceAsStream("files.txt");
        InputStreamReader isr = new InputStreamReader(is);
        BufferedReader br = new BufferedReader(isr);
        String line;
        while ((line = br.readLine()) != null)
        {
            System.out.println("Copying " + line);
            copyResourceToFile(line, destFolderPath + line);
        }
    }

    public static void copyResourceToFile(String resourcePath, String destPath) throws IOException {

        InputStream source = this.getClass().getResourceAsStream(resourcePath);
        Files.copy(source, Paths.get(destPath), StandardCopyOption.REPLACE_EXISTING);

    }
}