#!/usr/bin/env perl -w

#################################################
# Advent of Code 2022 - Elf ...
#################################################

use strict;
use warnings;

use Getopt::Long;					          # To easily retrieve arguments from command-line
use Term::ANSIColor qw(:constants);	# Colored output for the terminal

#### ------------Subroutines------------ ####

sub say 	{ print @_, "\n"; }
sub nice	{ say BOLD, BLUE,	"==> ", RESET, @_;}
sub oops	{ say BOLD, YELLOW,	"/!\\ ", RESET, @_;}
sub fail	{ say BOLD, RED,	"!!! ", RESET, @_;}

#### ------------Subroutines------------ ####

#### ---------------Input--------------- ####

my $prog = $0;
my $input;
my $help;
my $m_length = 4;

my $ok = GetOptions(
    'input=s'         => \$input,
    'marker_length=i' => \$m_length,
    'help'            => \$help,
);

my $usage = <<EOQ;
Usage for $0:
  >$prog [--input_list <input.txt> --marker_length <[0-9]+> --help]
EOQ

if ($help || !$ok ) {
    nice $usage;
    exit;
}

my $string = do {
    local $/ = undef;
    open my $fh, "<", $input or die "could not open $input: $!";
    <$fh>;
};

#### ---------------Input--------------- ####

#### -----------The real work----------- ####

for (my $i = 0; $i < length($string); $i++) {
    my $signal = substr($string, $i, $m_length);
    my @signal_chars = split(//, $signal);
    my %seen = ();
    my $seen = 0;
    foreach my $char (@signal_chars) {
        $seen{$char}++;
    }
    if (scalar keys %seen == $m_length) {
        my $result = index($string, $signal) + $m_length;
        nice $result;
        exit;
    }
}

#### -----------The real work----------- ####
