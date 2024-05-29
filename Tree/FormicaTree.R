library(ape)
library(phytools)

tree <- read.tree("TreeBorowiecEtAl.txt")
tree <- force.ultrametric(tree)
plot(tree)

sort(tree$tip.label)

tree_pruned <- drop.tip(tree, c("Rossomyrmex minuchae F0152",
                                "Proformica mongolica F0150"))

tree_pruned <- drop.tip(tree, c("Formica_adamsi_alpina_F0068",
                                "Formica_cf_altipetens_F0100",
                                "Formica_aserva_F0042",
                                "Formica_aserva_F0067",
                                "Formica_aserva_F0041",
                                "Formica_aserva_F0043",
                                "Formica_aserva_F0044",
                                "Formica_clara_F0118",
                                "Formica_dakotensis_F0069",
                                "Formica_dakotensis_F0071",
                                "Formica_densiventris_F0072",
                                "Formica_cf_densiventris_F0075",
                                "Formica_cf_densiventris_F0164",
                                "Formica_cf_densiventris_F007",
                                "Formica_dolosa_F0061",
                                "Formica_exsectoides_F0030",
                                "Formica_exsectoides_F0031",
                                "Formica_gnava_F0105",
                                "Formica_incerta_F0059",
                                "Formica_integroides_F0005",
                                "Formica_lasioides_F0036",
                                "Formica_mesasiatica_F0035",
                                "Formica_mlb01_micro_grp_F0082",
                                "Formica_mlb02_micro_grp_F0083",
                                "Formica_mlb03_micro_grp_F0084",
                                "Formica_mlb04_micro_grp_F0085",
                                "Formica_moki_F0129",
                                "Formica_neorufibarbis_F0109",
                                "Formica_neorufibarbis_F0127",
                                "Formica_neorufibarbis_F0128",
                                "Formica_neorufibarbis_t_F0108",
                                "Formica_neorufibarbis_t_F0126",
                                "Formica_nevadensis_F0079",
                                "Formica_nevadensis_F0080",
                                "Formica_obscuripes_F0008",
                                "Formica_obscuripes_F0009",
                                "Formica_obscuripes_F0162",
                                "Formica_obscuriventris_F0011",
                                "Formica_cf_fossaceps_F0004",
                                "Formica_obtusopilosa_F0047",
                                "Formica_oreas_F0012",
                                "Formica_oreas_F0013",
                                "Formica_oreas_F0125",
                                "Formica_pacifica_F0135",
                                "Formica_pallidefulva_F0066",
                                "Formica_nr_pergandei_F0051",
                                "Formica_podzolica_F0145",
                                "Formica_puberula_F0056",
                                "Formica_querquetulana_F0081",
                                "Formica_ravida_F0027",
                                "Formica_rubicunda_F0055",
                                "Formica_sanguinea_F0048",
                                "Formica_sp_fusca_grp_F0101",
                                "Formica_sp_fusca_grp_F0142",
                                "Formica_sp_fusca_grp_F0143",
                                "Formica_sp_fusca_grp_F0160",
                                "Formica_sp_fusca_grp_F0161",
                                "Formica_sp_fusca_grp_F0165",
                                "Formica_sp_micro_grp_F0074",
                                "Formica_sp_micro_grp_F0087",   
                                "Formica_sp_micro_grp_F0089",
                                "Formica_sp_micro_grp_F0090",
                                "Formica_sp_micro_grp_F0091",
                                "Formica_sp_micro_grp_F0092",
                                "Formica_sp_micro_grp_F0093",
                                "Formica_sp_micro_grp_F0094",
                                "Formica_sp_micro_grp_F0096",
                                "Formica_sp_micro_grp_F0157",  
                                "Formica_sp_neog_grp_F0058",
                                "Formica_sp_sang_grp_F0123",
                                "Formica_subnitens_F0025",
                                "Formica_cf_subnitens_F0014",
                                "Formica_subpolita_F0138",
                                "Formica_subsericea_F0144",
                                "Formica_subsericea_F0146",
                                "Formica_sibylla_F0132",
                                "Formica_talbotae_F0156",
                                "Formica_xerophila_F0139",
                                "Polyergus_longicornis_F0158",
                                "Polyergus_mexicanus_F0154",
                                "Polyergus_rufescens_F0149",
                                "Rossomyrmex_minuchae_F0152",
                                "Proformica_mongolica_F0150"
                                ))



# polyfiletic: 
#branchlength dakotensis "Formica_dakotensis_F0069" "Formica_dakotensis_F0070" "Formica_dakotensis_F0071"    
#branchlength gnava "Formica_gnava_F0105" "Formica_gnava_F0147"
#toplogy integroides "Formica_integroides_F0005" "Formica_integroides_F0114" 
#toplogy obscuriventris "Formica_obscuriventris_F0006" "Formica_obscuriventris_F0011"
#toplogy puberula "Formica_puberula_F0056" "Formica_puberula_F0122"
#toplogy ravida "Formica_ravida_F0026" "Formica_ravida_F0027"  
#toplogy rubicunda "Formica_rubicunda_F0054" "Formica_rubicunda_F0055"

tip.tmp <- gsub("_F[0-9]...", "", tree_pruned$tip.label)
tip.tmp <- gsub("cf", "", tip.tmp)
tip.tmp <- gsub("nr", "", tip.tmp)
tip.tmp <- gsub("__", "_", tip.tmp)

tree_pruned$tip.label <- tip.tmp

is.ultrametric(tree_pruned)
plot(tree_pruned)
sort(tree_pruned$tip.label)
