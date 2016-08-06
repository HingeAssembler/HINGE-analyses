/*
Copyright 2008-2010 Gephi
Authors : Mathieu Bastian <mathieu.bastian@gephi.org>
Website : http://www.gephi.org

This file is part of Gephi.

Gephi is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.

Gephi is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with Gephi.  If not, see <http://www.gnu.org/licenses/>.
 */
package org.gephi.toolkit.demos;

import java.awt.*;
import java.io.File;
import java.io.IOException;
import java.util.concurrent.TimeUnit;

import org.gephi.appearance.AttributeRankingImpl;
import org.gephi.appearance.RankingImpl;
import org.gephi.appearance.api.*;
import org.gephi.appearance.plugin.PartitionElementColorTransformer;
import org.gephi.appearance.plugin.RankingElementColorTransformer;
import org.gephi.appearance.plugin.palette.Palette;
import org.gephi.appearance.plugin.palette.PaletteManager;
import org.gephi.graph.api.*;
import org.gephi.io.exporter.api.ExportController;
import org.gephi.io.generator.plugin.RandomGraph;
import org.gephi.io.importer.api.Container;
import org.gephi.io.importer.api.EdgeDirectionDefault;
import org.gephi.io.importer.api.ImportController;
import org.gephi.io.processor.plugin.DefaultProcessor;
import org.gephi.layout.plugin.AutoLayout;
import org.gephi.layout.plugin.force.StepDisplacement;
import org.gephi.layout.plugin.force.yifanHu.YifanHuLayout;
import org.gephi.layout.plugin.forceAtlas.ForceAtlasLayout;
import org.gephi.layout.plugin.forceAtlas2.ForceAtlas2;
import org.gephi.preview.api.PreviewController;
import org.gephi.preview.api.PreviewModel;
import org.gephi.preview.api.PreviewProperty;
import org.gephi.preview.types.EdgeColor;
import org.gephi.project.api.ProjectController;
import org.gephi.project.api.Workspace;
import org.gephi.statistics.plugin.GraphDistance;
import org.openide.filesystems.AbstractFileSystem;
import org.openide.util.Lookup;
import org.gephi.datalab.api.AttributeColumnsController;

import org.gephi.appearance.api.Function;
import org.gephi.appearance.plugin.RankingElementColorTransformer;
import org.gephi.appearance.plugin.RankingNodeSizeTransformer;
import org.openide.util.actions.SystemAction;

/**
 * This demo shows how to use the <code>AutoLayout</code> class to run layout
 * programmatically.
 * <p>
 * You can set a layout duration, and an execution ratio for several layout. For
 * instance you set 0.8 for a Yifan Hu algorithm and 0.2 for Label Adjust. If
 * execution time is 100 seconds, the first algorithm run for 80 seconds and the
 * second for 20 seconds. It also allows to change property values dynamically
 * (at a certain ratio or interpolated if values are numerical).
 *
 * @author Mathieu Bastian
 */
public class WithAutoLayout {

    public void script(String input, String output, int time) {
        //Init a project - and therefore a workspace
        ProjectController pc = Lookup.getDefault().lookup(ProjectController.class);
        pc.newProject();
        Workspace workspace = pc.getCurrentWorkspace();

        //Generate a new random graph into a container
        Container container = Lookup.getDefault().lookup(Container.Factory.class).newContainer();
        //RandomGraph randomGraph = new RandomGraph();
        //randomGraph.setNumberOfNodes(500);
        //randomGraph.setWiringProbability(0.005);
        //randomGraph.generate(container.getLoader());
        ImportController importController = Lookup.getDefault().lookup(ImportController.class);


        try {
            File file = new File(input);
            container = importController.importFile(file);
            container.getLoader().setEdgeDefault(EdgeDirectionDefault.DIRECTED);   //Force DIRECTED
            container.getLoader().setAllowAutoNode(false);  //Don't create missing nodes
        } catch (Exception ex) {
            ex.printStackTrace();
            return;
        }

        AppearanceController appearanceController = Lookup.getDefault().lookup(AppearanceController.class);
        AppearanceModel appearanceModel = appearanceController.getModel();


        //Append container to graph structure
        importController.process(container, new DefaultProcessor(), workspace);

        //See if graph is well imported
        GraphModel graphModel = Lookup.getDefault().lookup(GraphController.class).getGraphModel();
        DirectedGraph graph = graphModel.getDirectedGraph();
        System.out.println("Nodes: " + graph.getNodeCount());
        System.out.println("Edges: " + graph.getEdgeCount());

        //Rank color by Degree


        GraphModel model = Lookup.getDefault().lookup(GraphController.class).getGraphModel();



        //List node columns
        for (Column col : model.getNodeTable()) {
            System.out.println("id:" + col.getId());
            System.out.println(col);
            //for (Node n : model.getGraph().getNodes()) {
            //    System.out.println(n.getAttribute(col));
            //}
        }

        for (Node n : model.getGraph().getNodes()) {
            System.out.println(n.getAttribute("d2"));
        }


        //Column colorCol = model.getNodeTable().getColumn("d1");


        for (Node n : model.getGraph().getNodes()) {
            n.setSize(new Float(30.0f));
            int r = (int)Float.parseFloat(n.getAttribute("d6").toString());
            int g = (int)Float.parseFloat(n.getAttribute("d0").toString());
            int b = (int)Float.parseFloat(n.getAttribute("d2").toString());

            System.out.print(r);
            System.out.print('\n');

            n.setColor(new Color(r,g,b));

        }


        //Column aln_col = model.getNodeTable().getColumn("d2");

        /*Function aln_ranking = appearanceModel.getNodeFunction(graph, aln_col, RankingElementColorTransformer.class);
        RankingElementColorTransformer degreeTransformer = (RankingElementColorTransformer) aln_ranking.getTransformer();
        degreeTransformer.setColors(new Color[]{new Color(0x7900BA), new Color(0x1C00BA), new Color(0xE88A00), new Color(0x0093BA),new Color(0x879495), new Color(0x04BA00)});
        degreeTransformer.setColorPositions(new float[]{0f, 0.2f, 0.4f, 0.6f, 0.8f, 1.0f});
        appearanceController.transform(aln_ranking);
        */

        //Layout for 1 minute
        AutoLayout autoLayout = new AutoLayout(time, TimeUnit.SECONDS);
        autoLayout.setGraphModel(graphModel);
        //YifanHuLayout firstLayout = new YifanHuLayout(null, new StepDisplacement(1f));
        ForceAtlas2 secondLayout = new ForceAtlas2(null);
        //AutoLayout.DynamicProperty adjustBySizeProperty = AutoLayout.createDynamicProperty("forceAtlas.adjustSizes.name", Boolean.TRUE, 0.1f);//True after 10% of layout time
        //AutoLayout.DynamicProperty repulsionProperty = AutoLayout.createDynamicProperty("forceAtlas.repulsionStrength.name", 500., 0f);//500 for the complete period
        autoLayout.addLayout(secondLayout, 1f);
        //autoLayout.addLayout(secondLayout, 0.5f, new AutoLayout.DynamicProperty[]{adjustBySizeProperty, repulsionProperty});
        autoLayout.execute();

        PreviewModel pmodel = Lookup.getDefault().lookup(PreviewController.class).getModel();
        pmodel.getProperties().putValue(PreviewProperty.NODE_BORDER_WIDTH, new Float(0f));
        pmodel.getProperties().putValue(PreviewProperty.EDGE_THICKNESS, new Float(0.1f));



        //Export
        ExportController ec = Lookup.getDefault().lookup(ExportController.class);
        try {
            ec.exportFile(new File(output+".png"));
            ec.exportFile(new File(output+".pdf"));
        } catch (IOException ex) {
            ex.printStackTrace();
        }

        secondLayout.endAlgo();





        Column column = graphModel.getNodeTable().getColumn("d1");
        Function func = appearanceModel.getNodeFunction(graph, column, PartitionElementColorTransformer.class);
        Partition partition = ((PartitionFunction) func).getPartition();
        Palette palette = PaletteManager.getInstance().generatePalette(partition.size());
        partition.setColors(palette.getColors());
        appearanceController.transform(func);



        try {
            ec.exportFile(new File(output+".contig.png"));
            ec.exportFile(new File(output+".contig.pdf"));
        } catch (IOException ex) {
            ex.printStackTrace();
        }




    }
}
